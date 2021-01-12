"""Configuration stuff."""

import yaml
import logging
import os
import sys
from pathlib import Path

import requests
import toml
from dotenv import load_dotenv
from pydantic.error_wrappers import ValidationError

from .model import Config

log = logging.getLogger(__name__)

load_dotenv()


def without_trailing_slash(url):
    """Strip trailing slash if exists."""
    return url[:-1] if url.endswith("/") else url


LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
numeric_log_level = getattr(logging, LOG_LEVEL.upper(), None)
if not isinstance(numeric_log_level, int):
    log.error("Invalid log level: %s", LOG_LEVEL)
logging.basicConfig(
    format="%(levelname)s:%(name)s:%(message)s",
    level=numeric_log_level,
    stream=sys.stderr,  # script outputs data
)

SECRET_KEY = os.environ.get("SECRET_KEY") or None

BADGE_CONFIG_URL = os.environ.get("BADGE_CONFIG_URL") or None
BADGE_CONFIG = None
if BADGE_CONFIG_URL is None:
    log.warning(
        "BADGE_CONFIG_URL environment variable is not set, disable badge feature"
    )
else:
    response = requests.get(BADGE_CONFIG_URL)
    if not response.ok:
        log.warning(
            "Can't retrieve badge config from [%s], disable badge feature",
            BADGE_CONFIG_URL,
        )
    else:
        BADGE_CONFIG = toml.loads(response.text)

SHIELDS_IO_BASE_URL = os.environ.get("SHIELDS_IO_BASE_URL") or None
if SHIELDS_IO_BASE_URL:
    SHIELDS_IO_BASE_URL = without_trailing_slash(SHIELDS_IO_BASE_URL)

CONFIG_FILE = os.environ.get("CONFIG_FILE") or None
if not CONFIG_FILE:
    log.error("CONFIG_FILE environment variable is not set, can't go further")

CONFIG = None
if CONFIG_FILE:
    CONFIG_FILE = Path(CONFIG_FILE)
    with CONFIG_FILE.open() as fd:
        try:
            config_dict = yaml.full_load(fd)
        except yaml.scanner.ScannerError as exc:
            raise ValueError(f"Could not load YAML config file {CONFIG_FILE}") from exc
        try:
            CONFIG = Config.parse_obj(config_dict)
        except ValidationError as exc:
            raise ValueError(f"Invalid config from {CONFIG_FILE}") from exc

MATOMO_BASE_URL = os.getenv("MATOMO_BASE_URL") or None
if MATOMO_BASE_URL:
    MATOMO_BASE_URL = without_trailing_slash(MATOMO_BASE_URL)
MATOMO_SITE_ID = os.getenv("MATOMO_SITE_ID") or None
if MATOMO_SITE_ID:
    MATOMO_SITE_ID = int(MATOMO_SITE_ID)

SENTRY_DSN = os.environ.get("SENTRY_DSN")

# PDF generation service
BROWSERLESS_API_URL = os.getenv("BROWSERLESS_API_URL") or None
BROWSERLESS_API_TOKEN = os.getenv("BROWSERLESS_API_TOKEN") or None
