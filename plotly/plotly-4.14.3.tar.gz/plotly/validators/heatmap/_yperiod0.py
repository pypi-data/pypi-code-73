import _plotly_utils.basevalidators


class Yperiod0Validator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="yperiod0", parent_name="heatmap", **kwargs):
        super(Yperiod0Validator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {"ytype": "scaled"}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
