import _plotly_utils.basevalidators


class RowValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name="row", parent_name="parcats.domain", **kwargs):
        super(RowValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
