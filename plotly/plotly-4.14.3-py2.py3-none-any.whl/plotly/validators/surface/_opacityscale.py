import _plotly_utils.basevalidators


class OpacityscaleValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="opacityscale", parent_name="surface", **kwargs):
        super(OpacityscaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
