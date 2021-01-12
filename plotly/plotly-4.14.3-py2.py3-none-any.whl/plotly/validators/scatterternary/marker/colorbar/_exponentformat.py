import _plotly_utils.basevalidators


class ExponentformatValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="exponentformat",
        parent_name="scatterternary.marker.colorbar",
        **kwargs
    ):
        super(ExponentformatValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["none", "e", "E", "power", "SI", "B"]),
            **kwargs
        )
