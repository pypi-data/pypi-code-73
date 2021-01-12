# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'InstanceMemcacheNode',
    'InstanceMemcacheParameters',
    'InstanceNodeConfig',
]

@pulumi.output_type
class InstanceMemcacheNode(dict):
    def __init__(__self__, *,
                 host: Optional[str] = None,
                 node_id: Optional[str] = None,
                 port: Optional[int] = None,
                 state: Optional[str] = None,
                 zone: Optional[str] = None):
        if host is not None:
            pulumi.set(__self__, "host", host)
        if node_id is not None:
            pulumi.set(__self__, "node_id", node_id)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def host(self) -> Optional[str]:
        return pulumi.get(self, "host")

    @property
    @pulumi.getter(name="nodeId")
    def node_id(self) -> Optional[str]:
        return pulumi.get(self, "node_id")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def zone(self) -> Optional[str]:
        return pulumi.get(self, "zone")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class InstanceMemcacheParameters(dict):
    def __init__(__self__, *,
                 id: Optional[str] = None,
                 params: Optional[Mapping[str, str]] = None):
        """
        :param str id: -
               This is a unique ID associated with this set of parameters.
        :param Mapping[str, str] params: User-defined set of parameters to use in the memcache process.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if params is not None:
            pulumi.set(__self__, "params", params)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        -
        This is a unique ID associated with this set of parameters.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def params(self) -> Optional[Mapping[str, str]]:
        """
        User-defined set of parameters to use in the memcache process.
        """
        return pulumi.get(self, "params")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class InstanceNodeConfig(dict):
    def __init__(__self__, *,
                 cpu_count: int,
                 memory_size_mb: int):
        """
        :param int cpu_count: Number of CPUs per node.
        :param int memory_size_mb: Memory size in Mebibytes for each memcache node.
        """
        pulumi.set(__self__, "cpu_count", cpu_count)
        pulumi.set(__self__, "memory_size_mb", memory_size_mb)

    @property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> int:
        """
        Number of CPUs per node.
        """
        return pulumi.get(self, "cpu_count")

    @property
    @pulumi.getter(name="memorySizeMb")
    def memory_size_mb(self) -> int:
        """
        Memory size in Mebibytes for each memcache node.
        """
        return pulumi.get(self, "memory_size_mb")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


