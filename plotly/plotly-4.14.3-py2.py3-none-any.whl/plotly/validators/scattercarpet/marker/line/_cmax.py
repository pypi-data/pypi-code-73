import _plotly_utils.basevalidators


class CmaxValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="cmax", parent_name="scattercarpet.marker.line", **kwargs
    ):
        super(CmaxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"cauto": False}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
