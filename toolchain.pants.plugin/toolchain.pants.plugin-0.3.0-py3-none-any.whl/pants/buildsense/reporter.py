# Copyright © 2020 Toolchain Labs, Inc. All rights reserved.
#
# Toolchain Labs, Inc. CONFIDENTIAL
#
# This file includes unpublished proprietary source code of Toolchain Labs, Inc.
# The copyright notice above does not evidence any actual or intended publication of such source code.
# Disclosure of this source code or any related proprietary information is strictly prohibited without
# the express written permission of Toolchain Labs, Inc.
import base64
import logging
import os
import re
import socket
import time
from pathlib import Path
from threading import Thread
from typing import Dict, List, Optional

from pants.base.build_environment import get_git
from pants.engine.rules import collect_rules, rule
from pants.engine.streaming_workunit_handler import (
    StreamingWorkunitContext,
    WorkunitsCallback,
    WorkunitsCallbackFactory,
    WorkunitsCallbackFactoryRequest,
)
from pants.engine.unions import UnionRule
from pants.option.option_value_container import OptionValueContainer
from pants.option.subsystem import Subsystem

from toolchain.pants.auth.store import AuthStore
from toolchain.pants.buildsense.client import BuildSenseClient
from toolchain.pants.buildsense.common import RunTrackerBuildInfo, WorkUnits, WorkUnitsMap
from toolchain.pants.buildsense.state import BuildState
from toolchain.pants.common.toolchain_setup import ToolchainSetup

logger = logging.getLogger(__name__)


_CI_MAP = {
    "CIRCLECI": re.compile(r"^CIRCLE.*"),
    "TRAVIS": re.compile(r"^TRAVIS.*"),
    "GITHUB_ACTION": re.compile(r"^GITHUB.*"),
}


def optional_dir_option(dn: str) -> str:
    # Similar to Pant's dir_option, but doesn't require the directory to exist.
    return os.path.normpath(dn)


class Reporter(Subsystem):
    options_scope = "buildsense"
    help = """Configuration for Toolchain's BuildSense reporting."""

    @classmethod
    def register_options(cls, register):
        register(
            "--base-url",
            advanced=True,
            type=str,
            default="https://app.toolchain.com/api/v1/repos/",
            help="Where to make HTTP requests to",
        )
        register(
            "--timeout",
            advanced=True,
            type=int,
            default=5,
            help="Wait at most this many seconds for network calls to complete.",
        )
        register("--dry-run", type=bool, help="Go thru the motions w/o making network calls", default=False)
        register(
            "--local-build-store",
            advanced=True,
            type=bool,
            default=True,
            help="Store failed uploads and try to upload later.",
        )
        register(
            "--local-store-base",
            advanced=True,
            type=optional_dir_option,
            default=".pants.d/toolchain/buildsense/",
            help="Base direcory for storing buildsense data locally",
        )
        register(
            "--max-batch-size-mb",
            advanced=True,
            type=int,
            default=20,
            help="Maximum batch size to try and upload (uncompressed).",
        )
        register(
            "--ci-env-var-pattern",
            advanced=True,
            type=str,
            default=None,
            help="CI Environment variables regex pattern.",
        )
        register(
            "--enable",
            type=bool,
            default=False,
            help="Enables the BuildSense reporter plugin",
        )


class ReporterCallback(WorkunitsCallback):
    """Configuration for Toolchain's BuildSense reporting."""

    def __init__(
        self,
        options: OptionValueContainer,
        auth_store: AuthStore,
        repo_name: Optional[str],
    ):
        super().__init__()
        self._enabled = False
        if not options.enable:
            logger.debug("BuildSense plugin is disabled.")
            return
        if not repo_name:
            logger.warning("Couldn't determine repo name. BuildSense plugin will be disabled.")
            return
        client = BuildSenseClient.from_options(client_options=options, auth=auth_store, repo=repo_name)
        # set self._build_state *before* changing the state.
        self._build_state = BuildState(
            client,
            local_store_base_path=Path(options.local_store_base),
            max_batch_size_mb=options.max_batch_size_mb,
            local_store_enabled=options.local_build_store,
        )

        self._enabled = True
        self._ci_regex_pattern = re.compile(options.ci_env_var_pattern) if options.ci_env_var_pattern else None
        self._call_count = 0
        self._reporter_thread = ReportThread(self._build_state)
        logger.debug("BuildSense Plugin enabled")

    def __call__(
        self,
        *,
        completed_workunits: WorkUnits,
        started_workunits: WorkUnits,
        context: StreamingWorkunitContext,
        finished: bool = False,
        **kwargs,
    ) -> None:
        if not self._enabled:
            return
        self.handle_workunits(
            completed_workunits=completed_workunits,
            started_workunits=started_workunits,
            context=context,
            finished=finished,
        )

    def handle_workunits(
        self,
        *,
        completed_workunits: WorkUnits,
        started_workunits: WorkUnits,
        context: StreamingWorkunitContext,
        finished: bool,
    ) -> None:
        work_units_map = {wu["span_id"]: wu for wu in (started_workunits or [])}
        work_units_map.update({wu["span_id"]: wu for wu in (completed_workunits or [])})
        logger.debug(
            f"handle_workunits total={len(work_units_map)} completed={len(completed_workunits)} started={len(started_workunits)} finished={finished} calls={self._call_count}"
        )
        self._build_state.set_context(context)
        if self._call_count == 0 and not finished:
            # If the first invocation of ReporterCallback by pants is also the last one
            # (i.e. if finished=True), then we don't send the initial report to buildsense.
            self._enqueue_initial_report(context)
        if finished:
            self._on_finish(context, self._call_count, work_units_map)
        else:
            self._build_state.queue_workunits(self._call_count, work_units_map)
        self._call_count += 1

    def _enqueue_initial_report(self, context: StreamingWorkunitContext) -> None:
        run_tracker_info = self._get_run_tracker_info(context)
        logger.debug(f"enqueue_initial_report {run_tracker_info.run_id}")
        self._build_state.queue_initial_report(run_tracker_info)

    def _on_finish(self, context: StreamingWorkunitContext, call_count: int, work_units_map: WorkUnitsMap) -> None:
        run_tracker_info = self._get_run_tracker_info(context)
        self._build_state.build_ended(run_tracker_info, call_count=call_count, work_units_map=work_units_map)
        self._reporter_thread.stop_thread()

    def _get_run_tracker_info(self, context: StreamingWorkunitContext) -> RunTrackerBuildInfo:
        ci_env = _capture_ci_env(os.environ, self._ci_regex_pattern)  # type: ignore[arg-type]
        run_tracker = context.run_tracker
        has_ended = run_tracker.has_ended()
        run_info = run_tracker.run_information()

        _adjust_run_info_fields(run_info, run_tracker.goals, has_ended)

        build_stats = {
            "run_info": run_info,
            "recorded_options": run_tracker.get_options_to_record(),
        }

        if ci_env:
            build_stats["ci_env"] = ci_env

        if has_ended:
            build_stats.update(
                {
                    "pantsd_stats": run_tracker.pantsd_scheduler_metrics,
                    "cumulative_timings": run_tracker.get_cumulative_timings(),
                }
            )

            if hasattr(context, "get_observation_histograms"):
                histograms_info = context.get_observation_histograms()
                version = histograms_info["version"]
                if version == 0:
                    build_stats["observation_histograms"] = {
                        "version": version,
                        "histograms": {
                            key: base64.b64encode(value).decode("ascii")
                            for key, value in histograms_info["histograms"].items()
                        },
                    }

                else:
                    logger.warning(f"Cannot encode internal metrics histograms: unexpected version {version}")

        log_file = Path(run_tracker.run_logs_file) if has_ended else None

        return RunTrackerBuildInfo(has_ended=has_ended, build_stats=build_stats, log_file=log_file)


def _adjust_run_info_fields(run_info: dict, goals: List[str], has_ended: bool) -> None:
    scm = get_git()
    revision = scm.commit_id
    host = socket.gethostname()
    machine = f"{host} [docker]" if _is_docker() else host
    run_info.update(machine=machine, revision=scm.commit_id, branch=scm.branch_name or revision)

    if "parent_build_id" in run_info:
        del run_info["parent_build_id"]

    run_info["computed_goals"] = goals
    if not has_ended:
        run_info["outcome"] = "NOT_AVAILABLE"


def _is_docker() -> bool:
    # Based on https://github.com/jaraco/jaraco.docker/blob/master/jaraco/docker.py
    # https://stackoverflow.com/a/49944991/38265
    cgroup = Path("/proc/self/cgroup")
    return Path("/.dockerenv").exists() or (cgroup.exists() and "docker" in cgroup.read_text("utf-8"))


class ReportThread:
    def __init__(self, build_state: BuildState) -> None:
        self._build_state = build_state
        self._terminate = False
        self._reporter_thread = Thread(target=self._report_loop, name="buildsense-reporter", daemon=True)
        self._reporter_thread.start()

    def stop_thread(self):
        self._terminate = True
        self._reporter_thread.join()

    def _report_loop(self):
        while not self._terminate:
            if self._build_state.send_report():
                # If we send something in this call, then we don't need to sleep.
                continue
            time.sleep(0.05)
        self._build_state.send_final_report()


def _get_pattern(env: Dict[str, str]) -> Optional[re.Pattern]:
    for ci_name, capture_expression in _CI_MAP.items():
        if ci_name in env:
            return capture_expression
    return None


def _capture_ci_env(env: Dict[str, str], pattern: Optional[re.Pattern]) -> Optional[Dict[str, str]]:
    pattern = pattern or _get_pattern(env)
    if not pattern:
        return None
    return {key: value for key, value in env.items() if pattern.match(key)}


class BuildsenseCallbackFactoryRequest:
    """A unique request type that is installed to trigger construction of our WorkunitsCallback."""


@rule
def construct_buildsense_callback(
    _: BuildsenseCallbackFactoryRequest,
    reporter: Reporter,
    toolchain_setup: ToolchainSetup,
    auth_store: AuthStore,
) -> WorkunitsCallbackFactory:
    repo_name = toolchain_setup.safe_get_repo_name()
    return WorkunitsCallbackFactory(
        lambda: ReporterCallback(
            reporter.options,
            auth_store=auth_store,
            repo_name=repo_name,
        )
    )


def rules():
    return [
        UnionRule(WorkunitsCallbackFactoryRequest, BuildsenseCallbackFactoryRequest),
        *collect_rules(),
    ]
