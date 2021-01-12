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


class StatsGroupTopAdmin(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.StatsGroupTopAdmin`.

    Details:
        - Layer: ``122``
        - ID: ``0x6014f412``

    Parameters:
        user_id: ``int`` ``32-bit``
        deleted: ``int`` ``32-bit``
        kicked: ``int`` ``32-bit``
        banned: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["user_id", "deleted", "kicked", "banned"]

    ID = 0x6014f412
    QUALNAME = "types.StatsGroupTopAdmin"

    def __init__(self, *, user_id: int, deleted: int, kicked: int, banned: int) -> None:
        self.user_id = user_id  # int
        self.deleted = deleted  # int
        self.kicked = kicked  # int
        self.banned = banned  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StatsGroupTopAdmin":
        # No flags
        
        user_id = Int.read(data)
        
        deleted = Int.read(data)
        
        kicked = Int.read(data)
        
        banned = Int.read(data)
        
        return StatsGroupTopAdmin(user_id=user_id, deleted=deleted, kicked=kicked, banned=banned)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(Int(self.user_id))
        
        data.write(Int(self.deleted))
        
        data.write(Int(self.kicked))
        
        data.write(Int(self.banned))
        
        return data.getvalue()
