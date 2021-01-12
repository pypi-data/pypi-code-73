import _plotly_utils.basevalidators


class CurrentbinValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="currentbin", parent_name="histogram.cumulative", **kwargs
    ):
        super(CurrentbinValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["include", "exclude", "half"]),
            **kwargs
        )
