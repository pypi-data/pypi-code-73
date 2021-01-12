import _plotly_utils.basevalidators


class AutorangeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="autorange", parent_name="carpet.baxis", **kwargs):
        super(AutorangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", [True, False, "reversed"]),
            **kwargs
        )
