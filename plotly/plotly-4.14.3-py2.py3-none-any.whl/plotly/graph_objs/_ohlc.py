from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Ohlc(_BaseTraceType):

    # class properties
    # --------------------
    _parent_path_str = ""
    _path_str = "ohlc"
    _valid_props = {
        "close",
        "closesrc",
        "customdata",
        "customdatasrc",
        "decreasing",
        "high",
        "highsrc",
        "hoverinfo",
        "hoverinfosrc",
        "hoverlabel",
        "hovertext",
        "hovertextsrc",
        "ids",
        "idssrc",
        "increasing",
        "legendgroup",
        "line",
        "low",
        "lowsrc",
        "meta",
        "metasrc",
        "name",
        "opacity",
        "open",
        "opensrc",
        "selectedpoints",
        "showlegend",
        "stream",
        "text",
        "textsrc",
        "tickwidth",
        "type",
        "uid",
        "uirevision",
        "visible",
        "x",
        "xaxis",
        "xcalendar",
        "xperiod",
        "xperiod0",
        "xperiodalignment",
        "xsrc",
        "yaxis",
    }

    # close
    # -----
    @property
    def close(self):
        """
        Sets the close values.
    
        The 'close' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["close"]

    @close.setter
    def close(self, val):
        self["close"] = val

    # closesrc
    # --------
    @property
    def closesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  close .
    
        The 'closesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["closesrc"]

    @closesrc.setter
    def closesrc(self, val):
        self["closesrc"] = val

    # customdata
    # ----------
    @property
    def customdata(self):
        """
        Assigns extra data each datum. This may be useful when
        listening to hover, click and selection events. Note that,
        "scatter" traces also appends customdata items in the markers
        DOM elements
    
        The 'customdata' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["customdata"]

    @customdata.setter
    def customdata(self, val):
        self["customdata"] = val

    # customdatasrc
    # -------------
    @property
    def customdatasrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  customdata
        .
    
        The 'customdatasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["customdatasrc"]

    @customdatasrc.setter
    def customdatasrc(self, val):
        self["customdatasrc"] = val

    # decreasing
    # ----------
    @property
    def decreasing(self):
        """
        The 'decreasing' property is an instance of Decreasing
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.ohlc.Decreasing`
          - A dict of string/value properties that will be passed
            to the Decreasing constructor
    
            Supported dict properties:
                
                line
                    :class:`plotly.graph_objects.ohlc.decreasing.Li
                    ne` instance or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.ohlc.Decreasing
        """
        return self["decreasing"]

    @decreasing.setter
    def decreasing(self, val):
        self["decreasing"] = val

    # high
    # ----
    @property
    def high(self):
        """
        Sets the high values.
    
        The 'high' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["high"]

    @high.setter
    def high(self, val):
        self["high"] = val

    # highsrc
    # -------
    @property
    def highsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  high .
    
        The 'highsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["highsrc"]

    @highsrc.setter
    def highsrc(self, val):
        self["highsrc"] = val

    # hoverinfo
    # ---------
    @property
    def hoverinfo(self):
        """
        Determines which trace information appear on hover. If `none`
        or `skip` are set, no information is displayed upon hovering.
        But, if `none` is set, click and hover events are still fired.
    
        The 'hoverinfo' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['x', 'y', 'z', 'text', 'name'] joined with '+' characters
            (e.g. 'x+y')
            OR exactly one of ['all', 'none', 'skip'] (e.g. 'skip')
          - A list or array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["hoverinfo"]

    @hoverinfo.setter
    def hoverinfo(self, val):
        self["hoverinfo"] = val

    # hoverinfosrc
    # ------------
    @property
    def hoverinfosrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  hoverinfo
        .
    
        The 'hoverinfosrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["hoverinfosrc"]

    @hoverinfosrc.setter
    def hoverinfosrc(self, val):
        self["hoverinfosrc"] = val

    # hoverlabel
    # ----------
    @property
    def hoverlabel(self):
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.ohlc.Hoverlabel`
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor
    
            Supported dict properties:
                
                align
                    Sets the horizontal alignment of the text
                    content within hover label box. Has an effect
                    only if the hover label text spans more two or
                    more lines
                alignsrc
                    Sets the source reference on Chart Studio Cloud
                    for  align .
                bgcolor
                    Sets the background color of the hover labels
                    for this trace
                bgcolorsrc
                    Sets the source reference on Chart Studio Cloud
                    for  bgcolor .
                bordercolor
                    Sets the border color of the hover labels for
                    this trace.
                bordercolorsrc
                    Sets the source reference on Chart Studio Cloud
                    for  bordercolor .
                font
                    Sets the font used in hover labels.
                namelength
                    Sets the default length (in number of
                    characters) of the trace name in the hover
                    labels for all traces. -1 shows the whole name
                    regardless of length. 0-3 shows the first 0-3
                    characters, and an integer >3 will show the
                    whole name if it is less than that many
                    characters, but if it is longer, will truncate
                    to `namelength - 3` characters and add an
                    ellipsis.
                namelengthsrc
                    Sets the source reference on Chart Studio Cloud
                    for  namelength .
                split
                    Show hover information (open, close, high, low)
                    in separate labels.

        Returns
        -------
        plotly.graph_objs.ohlc.Hoverlabel
        """
        return self["hoverlabel"]

    @hoverlabel.setter
    def hoverlabel(self, val):
        self["hoverlabel"] = val

    # hovertext
    # ---------
    @property
    def hovertext(self):
        """
        Same as `text`.
    
        The 'hovertext' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["hovertext"]

    @hovertext.setter
    def hovertext(self, val):
        self["hovertext"] = val

    # hovertextsrc
    # ------------
    @property
    def hovertextsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  hovertext
        .
    
        The 'hovertextsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["hovertextsrc"]

    @hovertextsrc.setter
    def hovertextsrc(self, val):
        self["hovertextsrc"] = val

    # ids
    # ---
    @property
    def ids(self):
        """
        Assigns id labels to each datum. These ids for object constancy
        of data points during animation. Should be an array of strings,
        not numbers or any other type.
    
        The 'ids' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["ids"]

    @ids.setter
    def ids(self, val):
        self["ids"] = val

    # idssrc
    # ------
    @property
    def idssrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  ids .
    
        The 'idssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["idssrc"]

    @idssrc.setter
    def idssrc(self, val):
        self["idssrc"] = val

    # increasing
    # ----------
    @property
    def increasing(self):
        """
        The 'increasing' property is an instance of Increasing
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.ohlc.Increasing`
          - A dict of string/value properties that will be passed
            to the Increasing constructor
    
            Supported dict properties:
                
                line
                    :class:`plotly.graph_objects.ohlc.increasing.Li
                    ne` instance or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.ohlc.Increasing
        """
        return self["increasing"]

    @increasing.setter
    def increasing(self, val):
        self["increasing"] = val

    # legendgroup
    # -----------
    @property
    def legendgroup(self):
        """
        Sets the legend group for this trace. Traces part of the same
        legend group hide/show at the same time when toggling legend
        items.
    
        The 'legendgroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["legendgroup"]

    @legendgroup.setter
    def legendgroup(self, val):
        self["legendgroup"] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.ohlc.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                dash
                    Sets the dash style of lines. Set to a dash
                    type string ("solid", "dot", "dash",
                    "longdash", "dashdot", or "longdashdot") or a
                    dash length list in px (eg "5px,10px,2px,2px").
                    Note that this style setting can also be set
                    per direction via `increasing.line.dash` and
                    `decreasing.line.dash`.
                width
                    [object Object] Note that this style setting
                    can also be set per direction via
                    `increasing.line.width` and
                    `decreasing.line.width`.

        Returns
        -------
        plotly.graph_objs.ohlc.Line
        """
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    # low
    # ---
    @property
    def low(self):
        """
        Sets the low values.
    
        The 'low' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["low"]

    @low.setter
    def low(self, val):
        self["low"] = val

    # lowsrc
    # ------
    @property
    def lowsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  low .
    
        The 'lowsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["lowsrc"]

    @lowsrc.setter
    def lowsrc(self, val):
        self["lowsrc"] = val

    # meta
    # ----
    @property
    def meta(self):
        """
        Assigns extra meta information associated with this trace that
        can be used in various text attributes. Attributes such as
        trace `name`, graph, axis and colorbar `title.text`, annotation
        `text` `rangeselector`, `updatemenues` and `sliders` `label`
        text all support `meta`. To access the trace `meta` values in
        an attribute in the same trace, simply use `%{meta[i]}` where
        `i` is the index or key of the `meta` item in question. To
        access trace `meta` in layout attributes, use
        `%{data[n[.meta[i]}` where `i` is the index or key of the
        `meta` and `n` is the trace index.
    
        The 'meta' property accepts values of any type

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["meta"]

    @meta.setter
    def meta(self, val):
        self["meta"] = val

    # metasrc
    # -------
    @property
    def metasrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  meta .
    
        The 'metasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["metasrc"]

    @metasrc.setter
    def metasrc(self, val):
        self["metasrc"] = val

    # name
    # ----
    @property
    def name(self):
        """
        Sets the trace name. The trace name appear as the legend item
        and on hover.
    
        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the trace.
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    # open
    # ----
    @property
    def open(self):
        """
        Sets the open values.
    
        The 'open' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["open"]

    @open.setter
    def open(self, val):
        self["open"] = val

    # opensrc
    # -------
    @property
    def opensrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  open .
    
        The 'opensrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["opensrc"]

    @opensrc.setter
    def opensrc(self, val):
        self["opensrc"] = val

    # selectedpoints
    # --------------
    @property
    def selectedpoints(self):
        """
        Array containing integer indices of selected points. Has an
        effect only for traces that support selections. Note that an
        empty array means an empty selection where the `unselected` are
        turned on for all points, whereas, any other non-array values
        means no selection all where the `selected` and `unselected`
        styles have no effect.
    
        The 'selectedpoints' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["selectedpoints"]

    @selectedpoints.setter
    def selectedpoints(self, val):
        self["selectedpoints"] = val

    # showlegend
    # ----------
    @property
    def showlegend(self):
        """
        Determines whether or not an item corresponding to this trace
        is shown in the legend.
    
        The 'showlegend' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showlegend"]

    @showlegend.setter
    def showlegend(self, val):
        self["showlegend"] = val

    # stream
    # ------
    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.ohlc.Stream`
          - A dict of string/value properties that will be passed
            to the Stream constructor
    
            Supported dict properties:
                
                maxpoints
                    Sets the maximum number of points to keep on
                    the plots from an incoming stream. If
                    `maxpoints` is set to 50, only the newest 50
                    points will be displayed on the plot.
                token
                    The stream id number links a data trace on a
                    plot with a stream. See https://chart-
                    studio.plotly.com/settings for more details.

        Returns
        -------
        plotly.graph_objs.ohlc.Stream
        """
        return self["stream"]

    @stream.setter
    def stream(self, val):
        self["stream"] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets hover text elements associated with each sample point. If
        a single string, the same string appears over all the data
        points. If an array of string, the items are mapped in order to
        this trace's sample points.
    
        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["text"]

    @text.setter
    def text(self, val):
        self["text"] = val

    # textsrc
    # -------
    @property
    def textsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  text .
    
        The 'textsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["textsrc"]

    @textsrc.setter
    def textsrc(self, val):
        self["textsrc"] = val

    # tickwidth
    # ---------
    @property
    def tickwidth(self):
        """
        Sets the width of the open/close tick marks relative to the "x"
        minimal interval.
    
        The 'tickwidth' property is a number and may be specified as:
          - An int or float in the interval [0, 0.5]

        Returns
        -------
        int|float
        """
        return self["tickwidth"]

    @tickwidth.setter
    def tickwidth(self, val):
        self["tickwidth"] = val

    # uid
    # ---
    @property
    def uid(self):
        """
        Assign an id to this trace, Use this to provide object
        constancy between traces during animations and transitions.
    
        The 'uid' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["uid"]

    @uid.setter
    def uid(self, val):
        self["uid"] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of some user-driven changes to the trace:
        `constraintrange` in `parcoords` traces, as well as some
        `editable: true` modifications such as `name` and
        `colorbar.title`. Defaults to `layout.uirevision`. Note that
        other user-driven trace attribute changes are controlled by
        `layout` attributes: `trace.visible` is controlled by
        `layout.legend.uirevision`, `selectedpoints` is controlled by
        `layout.selectionrevision`, and `colorbar.(x|y)` (accessible
        with `config: {editable: true}`) is controlled by
        `layout.editrevision`. Trace changes are tracked by `uid`,
        which only falls back on trace index if no `uid` is provided.
        So if your app can add/remove traces before the end of the
        `data` array, such that the same trace has a different index,
        you can still preserve user-driven changes if you give each
        trace a `uid` that stays with it as it moves.
    
        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this trace is visible. If
        "legendonly", the trace is not drawn, but can appear as a
        legend item (provided that the legend itself is visible).
    
        The 'visible' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, False, 'legendonly']

        Returns
        -------
        Any
        """
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the x coordinates. If absent, linear coordinate will be
        generated.
    
        The 'x' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    # xaxis
    # -----
    @property
    def xaxis(self):
        """
        Sets a reference between this trace's x coordinates and a 2D
        cartesian x axis. If "x" (the default value), the x coordinates
        refer to `layout.xaxis`. If "x2", the x coordinates refer to
        `layout.xaxis2`, and so on.
    
        The 'xaxis' property is an identifier of a particular
        subplot, of type 'x', that may be specified as the string 'x'
        optionally followed by an integer >= 1
        (e.g. 'x', 'x1', 'x2', 'x3', etc.)

        Returns
        -------
        str
        """
        return self["xaxis"]

    @xaxis.setter
    def xaxis(self, val):
        self["xaxis"] = val

    # xcalendar
    # ---------
    @property
    def xcalendar(self):
        """
        Sets the calendar system to use with `x` date data.
    
        The 'xcalendar' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['gregorian', 'chinese', 'coptic', 'discworld',
                'ethiopian', 'hebrew', 'islamic', 'julian', 'mayan',
                'nanakshahi', 'nepali', 'persian', 'jalali', 'taiwan',
                'thai', 'ummalqura']

        Returns
        -------
        Any
        """
        return self["xcalendar"]

    @xcalendar.setter
    def xcalendar(self, val):
        self["xcalendar"] = val

    # xperiod
    # -------
    @property
    def xperiod(self):
        """
        Only relevant when the axis `type` is "date". Sets the period
        positioning in milliseconds or "M<n>" on the x axis. Special
        values in the form of "M<n>" could be used to declare the
        number of months. In this case `n` must be a positive integer.
    
        The 'xperiod' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["xperiod"]

    @xperiod.setter
    def xperiod(self, val):
        self["xperiod"] = val

    # xperiod0
    # --------
    @property
    def xperiod0(self):
        """
        Only relevant when the axis `type` is "date". Sets the base for
        period positioning in milliseconds or date string on the x0
        axis. When `x0period` is round number of weeks, the `x0period0`
        by default would be on a Sunday i.e. 2000-01-02, otherwise it
        would be at 2000-01-01.
    
        The 'xperiod0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["xperiod0"]

    @xperiod0.setter
    def xperiod0(self, val):
        self["xperiod0"] = val

    # xperiodalignment
    # ----------------
    @property
    def xperiodalignment(self):
        """
        Only relevant when the axis `type` is "date". Sets the
        alignment of data points on the x axis.
    
        The 'xperiodalignment' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['start', 'middle', 'end']

        Returns
        -------
        Any
        """
        return self["xperiodalignment"]

    @xperiodalignment.setter
    def xperiodalignment(self, val):
        self["xperiodalignment"] = val

    # xsrc
    # ----
    @property
    def xsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  x .
    
        The 'xsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["xsrc"]

    @xsrc.setter
    def xsrc(self, val):
        self["xsrc"] = val

    # yaxis
    # -----
    @property
    def yaxis(self):
        """
        Sets a reference between this trace's y coordinates and a 2D
        cartesian y axis. If "y" (the default value), the y coordinates
        refer to `layout.yaxis`. If "y2", the y coordinates refer to
        `layout.yaxis2`, and so on.
    
        The 'yaxis' property is an identifier of a particular
        subplot, of type 'y', that may be specified as the string 'y'
        optionally followed by an integer >= 1
        (e.g. 'y', 'y1', 'y2', 'y3', etc.)

        Returns
        -------
        str
        """
        return self["yaxis"]

    @yaxis.setter
    def yaxis(self, val):
        self["yaxis"] = val

    # type
    # ----
    @property
    def type(self):
        return self._props["type"]

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        close
            Sets the close values.
        closesrc
            Sets the source reference on Chart Studio Cloud for
            close .
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        decreasing
            :class:`plotly.graph_objects.ohlc.Decreasing` instance
            or dict with compatible properties
        high
            Sets the high values.
        highsrc
            Sets the source reference on Chart Studio Cloud for
            high .
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.ohlc.Hoverlabel` instance
            or dict with compatible properties
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        increasing
            :class:`plotly.graph_objects.ohlc.Increasing` instance
            or dict with compatible properties
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            :class:`plotly.graph_objects.ohlc.Line` instance or
            dict with compatible properties
        low
            Sets the low values.
        lowsrc
            Sets the source reference on Chart Studio Cloud for
            low .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        open
            Sets the open values.
        opensrc
            Sets the source reference on Chart Studio Cloud for
            open .
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.ohlc.Stream` instance or
            dict with compatible properties
        text
            Sets hover text elements associated with each sample
            point. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to this trace's sample points.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        tickwidth
            Sets the width of the open/close tick marks relative to
            the "x" minimal interval.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates. If absent, linear coordinate
            will be generated.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the x
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        xperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the x0 axis. When `x0period` is round number
            of weeks, the `x0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        xperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the x axis.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        """

    def __init__(
        self,
        arg=None,
        close=None,
        closesrc=None,
        customdata=None,
        customdatasrc=None,
        decreasing=None,
        high=None,
        highsrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        increasing=None,
        legendgroup=None,
        line=None,
        low=None,
        lowsrc=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        open=None,
        opensrc=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textsrc=None,
        tickwidth=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xaxis=None,
        xcalendar=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        yaxis=None,
        **kwargs
    ):
        """
        Construct a new Ohlc object
        
        The ohlc (short for Open-High-Low-Close) is a style of
        financial chart describing open, high, low and close for a
        given `x` coordinate (most likely time). The tip of the lines
        represent the `low` and `high` values and the horizontal
        segments represent the `open` and `close` values. Sample points
        where the close value is higher (lower) then the open value are
        called increasing (decreasing). By default, increasing items
        are drawn in green whereas decreasing are drawn in red.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.Ohlc`
        close
            Sets the close values.
        closesrc
            Sets the source reference on Chart Studio Cloud for
            close .
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        decreasing
            :class:`plotly.graph_objects.ohlc.Decreasing` instance
            or dict with compatible properties
        high
            Sets the high values.
        highsrc
            Sets the source reference on Chart Studio Cloud for
            high .
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.ohlc.Hoverlabel` instance
            or dict with compatible properties
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        increasing
            :class:`plotly.graph_objects.ohlc.Increasing` instance
            or dict with compatible properties
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            :class:`plotly.graph_objects.ohlc.Line` instance or
            dict with compatible properties
        low
            Sets the low values.
        lowsrc
            Sets the source reference on Chart Studio Cloud for
            low .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        open
            Sets the open values.
        opensrc
            Sets the source reference on Chart Studio Cloud for
            open .
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.ohlc.Stream` instance or
            dict with compatible properties
        text
            Sets hover text elements associated with each sample
            point. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to this trace's sample points.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        tickwidth
            Sets the width of the open/close tick marks relative to
            the "x" minimal interval.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates. If absent, linear coordinate
            will be generated.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the x
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        xperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the x0 axis. When `x0period` is round number
            of weeks, the `x0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        xperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the x axis.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.

        Returns
        -------
        Ohlc
        """
        super(Ohlc, self).__init__("ohlc")

        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.Ohlc 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.Ohlc`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("close", None)
        _v = close if close is not None else _v
        if _v is not None:
            self["close"] = _v
        _v = arg.pop("closesrc", None)
        _v = closesrc if closesrc is not None else _v
        if _v is not None:
            self["closesrc"] = _v
        _v = arg.pop("customdata", None)
        _v = customdata if customdata is not None else _v
        if _v is not None:
            self["customdata"] = _v
        _v = arg.pop("customdatasrc", None)
        _v = customdatasrc if customdatasrc is not None else _v
        if _v is not None:
            self["customdatasrc"] = _v
        _v = arg.pop("decreasing", None)
        _v = decreasing if decreasing is not None else _v
        if _v is not None:
            self["decreasing"] = _v
        _v = arg.pop("high", None)
        _v = high if high is not None else _v
        if _v is not None:
            self["high"] = _v
        _v = arg.pop("highsrc", None)
        _v = highsrc if highsrc is not None else _v
        if _v is not None:
            self["highsrc"] = _v
        _v = arg.pop("hoverinfo", None)
        _v = hoverinfo if hoverinfo is not None else _v
        if _v is not None:
            self["hoverinfo"] = _v
        _v = arg.pop("hoverinfosrc", None)
        _v = hoverinfosrc if hoverinfosrc is not None else _v
        if _v is not None:
            self["hoverinfosrc"] = _v
        _v = arg.pop("hoverlabel", None)
        _v = hoverlabel if hoverlabel is not None else _v
        if _v is not None:
            self["hoverlabel"] = _v
        _v = arg.pop("hovertext", None)
        _v = hovertext if hovertext is not None else _v
        if _v is not None:
            self["hovertext"] = _v
        _v = arg.pop("hovertextsrc", None)
        _v = hovertextsrc if hovertextsrc is not None else _v
        if _v is not None:
            self["hovertextsrc"] = _v
        _v = arg.pop("ids", None)
        _v = ids if ids is not None else _v
        if _v is not None:
            self["ids"] = _v
        _v = arg.pop("idssrc", None)
        _v = idssrc if idssrc is not None else _v
        if _v is not None:
            self["idssrc"] = _v
        _v = arg.pop("increasing", None)
        _v = increasing if increasing is not None else _v
        if _v is not None:
            self["increasing"] = _v
        _v = arg.pop("legendgroup", None)
        _v = legendgroup if legendgroup is not None else _v
        if _v is not None:
            self["legendgroup"] = _v
        _v = arg.pop("line", None)
        _v = line if line is not None else _v
        if _v is not None:
            self["line"] = _v
        _v = arg.pop("low", None)
        _v = low if low is not None else _v
        if _v is not None:
            self["low"] = _v
        _v = arg.pop("lowsrc", None)
        _v = lowsrc if lowsrc is not None else _v
        if _v is not None:
            self["lowsrc"] = _v
        _v = arg.pop("meta", None)
        _v = meta if meta is not None else _v
        if _v is not None:
            self["meta"] = _v
        _v = arg.pop("metasrc", None)
        _v = metasrc if metasrc is not None else _v
        if _v is not None:
            self["metasrc"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v
        _v = arg.pop("open", None)
        _v = open if open is not None else _v
        if _v is not None:
            self["open"] = _v
        _v = arg.pop("opensrc", None)
        _v = opensrc if opensrc is not None else _v
        if _v is not None:
            self["opensrc"] = _v
        _v = arg.pop("selectedpoints", None)
        _v = selectedpoints if selectedpoints is not None else _v
        if _v is not None:
            self["selectedpoints"] = _v
        _v = arg.pop("showlegend", None)
        _v = showlegend if showlegend is not None else _v
        if _v is not None:
            self["showlegend"] = _v
        _v = arg.pop("stream", None)
        _v = stream if stream is not None else _v
        if _v is not None:
            self["stream"] = _v
        _v = arg.pop("text", None)
        _v = text if text is not None else _v
        if _v is not None:
            self["text"] = _v
        _v = arg.pop("textsrc", None)
        _v = textsrc if textsrc is not None else _v
        if _v is not None:
            self["textsrc"] = _v
        _v = arg.pop("tickwidth", None)
        _v = tickwidth if tickwidth is not None else _v
        if _v is not None:
            self["tickwidth"] = _v
        _v = arg.pop("uid", None)
        _v = uid if uid is not None else _v
        if _v is not None:
            self["uid"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        _v = arg.pop("x", None)
        _v = x if x is not None else _v
        if _v is not None:
            self["x"] = _v
        _v = arg.pop("xaxis", None)
        _v = xaxis if xaxis is not None else _v
        if _v is not None:
            self["xaxis"] = _v
        _v = arg.pop("xcalendar", None)
        _v = xcalendar if xcalendar is not None else _v
        if _v is not None:
            self["xcalendar"] = _v
        _v = arg.pop("xperiod", None)
        _v = xperiod if xperiod is not None else _v
        if _v is not None:
            self["xperiod"] = _v
        _v = arg.pop("xperiod0", None)
        _v = xperiod0 if xperiod0 is not None else _v
        if _v is not None:
            self["xperiod0"] = _v
        _v = arg.pop("xperiodalignment", None)
        _v = xperiodalignment if xperiodalignment is not None else _v
        if _v is not None:
            self["xperiodalignment"] = _v
        _v = arg.pop("xsrc", None)
        _v = xsrc if xsrc is not None else _v
        if _v is not None:
            self["xsrc"] = _v
        _v = arg.pop("yaxis", None)
        _v = yaxis if yaxis is not None else _v
        if _v is not None:
            self["yaxis"] = _v

        # Read-only literals
        # ------------------

        self._props["type"] = "ohlc"
        arg.pop("type", None)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
