import _plotly_utils.basevalidators


class YanchorValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="yanchor", parent_name="scattergeo.marker.colorbar", **kwargs
    ):
        super(YanchorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["top", "middle", "bottom"]),
            **kwargs
        )
