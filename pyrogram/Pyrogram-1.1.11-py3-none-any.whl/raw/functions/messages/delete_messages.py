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


class DeleteMessages(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``122``
        - ID: ``0xe58e95d2``

    Parameters:
        id: List of ``int`` ``32-bit``
        revoke (optional): ``bool``

    Returns:
        :obj:`messages.AffectedMessages <pyrogram.raw.base.messages.AffectedMessages>`
    """

    __slots__: List[str] = ["id", "revoke"]

    ID = 0xe58e95d2
    QUALNAME = "functions.messages.DeleteMessages"

    def __init__(self, *, id: List[int], revoke: Union[None, bool] = None) -> None:
        self.id = id  # Vector<int>
        self.revoke = revoke  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "DeleteMessages":
        flags = Int.read(data)
        
        revoke = True if flags & (1 << 0) else False
        id = TLObject.read(data, Int)
        
        return DeleteMessages(id=id, revoke=revoke)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.revoke else 0
        data.write(Int(flags))
        
        data.write(Vector(self.id, Int))
        
        return data.getvalue()
