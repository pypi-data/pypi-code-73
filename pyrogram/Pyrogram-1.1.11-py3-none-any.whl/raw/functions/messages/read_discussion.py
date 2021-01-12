#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2021 Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Union, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class ReadDiscussion(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``122``
        - ID: ``0xf731a9f4``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        msg_id: ``int`` ``32-bit``
        read_max_id: ``int`` ``32-bit``

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "msg_id", "read_max_id"]

    ID = 0xf731a9f4
    QUALNAME = "functions.messages.ReadDiscussion"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, read_max_id: int) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.read_max_id = read_max_id  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ReadDiscussion":
        # No flags
        
        peer = TLObject.read(data)
        
        msg_id = Int.read(data)
        
        read_max_id = Int.read(data)
        
        return ReadDiscussion(peer=peer, msg_id=msg_id, read_max_id=read_max_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(self.peer.write())
        
        data.write(Int(self.msg_id))
        
        data.write(Int(self.read_max_id))
        
        return data.getvalue()
