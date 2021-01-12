"""EBUS Message Decoding."""
import re

from .msg import BrokenMsg, Field, Msg
from .na import NA


class MsgDecoder:

    """
    Message Decoder.

    Args:
        msgdefs (MsgDefs): Message Definitions
    """

    _re_decode = re.compile(r"([A-z0-9]+(\.[A-z0-9]+)?) ([^\s]*) (= )?(.*)")

    def __init__(self, msgdefs):
        self.msgdefs = msgdefs

    def decode_line(self, line):
        """
        Decode `line` and return :any:`Msg` instance.

        Raises:
            ValueError: if `line` does not match expected format.
            UnknownMsgError: if `line` is not covered by fields.
        """
        match = self._re_decode.match(line)
        if not match:
            raise ValueError(line)
        circuit, _, name, _, valuestr = match.groups()
        msgdef = self.msgdefs.get(circuit, name)
        if not msgdef:
            raise UnknownMsgError(f"circuit={circuit}, name={name}")
        return self.decode_value(msgdef, valuestr.strip())

    def decode_value(self, msgdef, valuestr):
        """Decode message `msgdef` valuestr `valuestr`."""
        if valuestr and "ERR: " not in valuestr:
            fields = tuple(self._decodefields(msgdef, valuestr.strip()))
            return Msg(msgdef, fields)
        else:
            return BrokenMsg(msgdef, valuestr.strip())

    @staticmethod
    def _decodefields(msgdef, valuestr):
        if valuestr not in ("no data stored", "nosignal"):
            values = valuestr.split(";")
            fields = []
            for fielddef in msgdef.fields:
                if fielddef.idx is None:
                    continue
                try:
                    value = values[fielddef.idx].strip()
                except IndexError:
                    fieldvalue = NA
                else:
                    try:
                        fieldvalue = fielddef.type_.decode(value)
                    except ValueError:
                        fieldvalue = None
                fields.append(Field(fielddef, fieldvalue))
        else:
            fields = [Field(fielddef, NA) for fielddef in msgdef.fields]
        # virtual fields
        for virtfielddef in msgdef.virtfields:
            virtfieldvalue = virtfielddef.func(fields)
            fields.append(Field(virtfielddef, virtfieldvalue))
        return fields


class UnknownMsgError(RuntimeError):

    """Exception raised in case of unknown Message."""
