"""EBUS Messages And Their Fields."""
import collections

from .na import NA
from .util import repr_

Error = collections.namedtuple("Error", "msg")


class Msg(collections.namedtuple("_Msg", "msgdef fields")):

    """Message With Fields."""

    __slots__ = tuple()

    valid = True

    def __repr__(self):
        args = (self.msgdef.name, self.fields)
        return repr_(self, args)

    @property
    def ident(self):
        """Identifier."""
        return self.msgdef.ident


class Field(collections.namedtuple("_Field", "fielddef value")):

    """Field with Data."""

    __slots__ = tuple()

    def __repr__(self):
        args = (self.fielddef.name, self.value)
        return repr_(self, args)

    @property
    def ident(self):
        """Identifier."""
        return self.fielddef.ident

    @property
    def unitvalue(self):
        """Unitized Value."""
        value = self.value
        if value is not None and value is not NA and not isinstance(value, str) and self.fielddef.unit:
            return f"{value} {self.fielddef.unit}"
        else:
            return value


def filter_msg(msg, msgdefs):
    """Strip Down Message to `msgdefs`."""
    ident = msg.msgdef.ident
    for msgdef in msgdefs:
        if ident == msgdef.ident:
            if msg.msgdef == msgdef:
                return msg
            else:
                fields = tuple(
                    Field(field.fielddef, field.value) for field in msg.fields if field.fielddef in msgdef.fields
                )
                return Msg(msgdef, fields)
    return None


class BrokenMsg:

    """
    Broken Message.

    .. note: In a boolean context this instance evaluates to `False`.
    """

    valid = False

    def __init__(self, msgdef, error):
        self.msgdef = msgdef
        self.error = error

    def __repr__(self):
        return repr_(self, (self.msgdef.ident, self.error))
