import sys

if sys.version_info < (3, 7):
    from ._colorbar import ColorBar
    from ._hoverlabel import Hoverlabel
    from ._marker import Marker
    from ._selected import Selected
    from ._stream import Stream
    from ._unselected import Unselected
    from . import colorbar
    from . import hoverlabel
    from . import marker
    from . import selected
    from . import unselected
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".colorbar", ".hoverlabel", ".marker", ".selected", ".unselected"],
        [
            "._colorbar.ColorBar",
            "._hoverlabel.Hoverlabel",
            "._marker.Marker",
            "._selected.Selected",
            "._stream.Stream",
            "._unselected.Unselected",
        ],
    )
