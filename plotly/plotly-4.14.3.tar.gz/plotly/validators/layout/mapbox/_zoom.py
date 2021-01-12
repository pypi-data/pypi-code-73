import _plotly_utils.basevalidators


class ZoomValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="zoom", parent_name="layout.mapbox", **kwargs):
        super(ZoomValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
