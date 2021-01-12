import _plotly_utils.basevalidators


class EnabledValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="enabled", parent_name="layout.xaxis.tickformatstop", **kwargs
    ):
        super(EnabledValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "ticks"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
