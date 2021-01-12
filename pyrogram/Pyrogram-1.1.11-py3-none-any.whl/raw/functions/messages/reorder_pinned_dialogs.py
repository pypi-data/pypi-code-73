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


class ReorderPinnedDialogs(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``122``
        - ID: ``0x3b1adf37``

    Parameters:
        folder_id: ``int`` ``32-bit``
        order: List of :obj:`InputDialogPeer <pyrogram.raw.base.InputDialogPeer>`
        force (optional): ``bool``

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["folder_id", "order", "force"]

    ID = 0x3b1adf37
    QUALNAME = "functions.messages.ReorderPinnedDialogs"

    def __init__(self, *, folder_id: int, order: List["raw.base.InputDialogPeer"], force: Union[None, bool] = None) -> None:
        self.folder_id = folder_id  # int
        self.order = order  # Vector<InputDialogPeer>
        self.force = force  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ReorderPinnedDialogs":
        flags = Int.read(data)
        
        force = True if flags & (1 << 0) else False
        folder_id = Int.read(data)
        
        order = TLObject.read(data)
        
        return ReorderPinnedDialogs(folder_id=folder_id, order=order, force=force)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.force else 0
        data.write(Int(flags))
        
        data.write(Int(self.folder_id))
        
        data.write(Vector(self.order))
        
        return data.getvalue()
