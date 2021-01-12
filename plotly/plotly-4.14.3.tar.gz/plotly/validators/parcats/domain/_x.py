import _plotly_utils.basevalidators


class XValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name="x", parent_name="parcats.domain", **kwargs):
        super(XValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            items=kwargs.pop(
                "items",
                [
                    {"valType": "number", "min": 0, "max": 1, "editType": "calc"},
                    {"valType": "number", "min": 0, "max": 1, "editType": "calc"},
                ],
            ),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
