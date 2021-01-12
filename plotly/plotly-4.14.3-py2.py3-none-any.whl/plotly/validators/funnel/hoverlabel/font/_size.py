import _plotly_utils.basevalidators


class SizeValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="size", parent_name="funnel.hoverlabel.font", **kwargs
    ):
        super(SizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "none"),
            min=kwargs.pop("min", 1),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
