import logging

import cachecontrol
import flask
import frictionless
import jinja2
import opendataschema
import pkg_resources
import requests
from commonmark import commonmark
from pydantic import HttpUrl

from . import config
from . import pdf_renderer

log = logging.getLogger(__name__)


def generate_schema_from_url_func(session):
    """Generates a function that encloses session"""

    def fetch_schema(url):
        response = session.get(url)
        response.raise_for_status()
        descriptor = response.json()
        return frictionless.Schema(descriptor)

    return fetch_schema


class SchemaCatalogRegistry:
    """Retain section_name -> catalog url matching
    and creates SchemaCatalog instance on demand"""

    def __init__(self, session):
        self.session = session
        self.ref_map = {}

    def add_ref(self, name, ref):
        self.ref_map[name] = ref

    def build_schema_catalog(self, name):
        ref = self.ref_map.get(name)
        if not ref:
            return None
        return opendataschema.SchemaCatalog(ref, session=self.session)


caching_session = cachecontrol.CacheControl(requests.Session())
fetch_schema = generate_schema_from_url_func(caching_session)

# And load schema catalogs which URLs are found in 'homepage' key of config.yaml
schema_catalog_registry = SchemaCatalogRegistry(caching_session)
if config.CONFIG:
    log.info("Initializing homepage sections...")
    for section in config.CONFIG.homepage.sections:
        name = section.name
        log.info('Initializing homepage section "{}"...'.format(name))
        if section.catalog:
            catalog_ref = (
                str(section.catalog)
                if isinstance(section.catalog, HttpUrl)
                else section.catalog.dict()
            )
            schema_catalog_registry.add_ref(name, catalog_ref)
    log.info("...done")


def configure_sentry(app):
    """Configure sentry.io service for application error monitoring."""

    sentry_dsn = app.config.get("SENTRY_DSN")
    if sentry_dsn:
        import sentry_sdk
        from sentry_sdk.integrations.flask import FlaskIntegration

        sentry_sdk.init(dsn=sentry_dsn, integrations=[FlaskIntegration()])


# Flask things
app = flask.Flask(__name__)
app.secret_key = config.SECRET_KEY
configure_sentry(app)


# Jinja2 url_quote_plus custom filter
# https://stackoverflow.com/questions/12288454/how-to-import-custom-jinja2-filters-from-another-file-and-using-flask
blueprint = flask.Blueprint("filters", __name__)


@jinja2.contextfilter
@blueprint.app_template_filter()
def commonmark2html(context, value):
    if not value:
        return value
    try:
        return commonmark(value)
    except Exception as ex:
        log.exception(ex)
        return value


app.register_blueprint(blueprint)


@app.context_processor
def inject_version():
    return {
        "validata_ui_version": pkg_resources.get_distribution("validata-ui").version
    }


@app.context_processor
def inject_config():
    return {"config": config}


# Used to generate PDF validation report
# If None, PDF report is not available
pdf_service = pdf_renderer.PDFRenderer.create_renderer_from_config(config)

# Keep this import after app initialisation (to avoid cyclic imports)
from . import views  # noqa isort:skip
