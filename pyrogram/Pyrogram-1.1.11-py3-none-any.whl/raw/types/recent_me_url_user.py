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


class RecentMeUrlUser(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.RecentMeUrl`.

    Details:
        - Layer: ``122``
        - ID: ``0x8dbc3336``

    Parameters:
        url: ``str``
        user_id: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["url", "user_id"]

    ID = 0x8dbc3336
    QUALNAME = "types.RecentMeUrlUser"

    def __init__(self, *, url: str, user_id: int) -> None:
        self.url = url  # string
        self.user_id = user_id  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "RecentMeUrlUser":
        # No flags
        
        url = String.read(data)
        
        user_id = Int.read(data)
        
        return RecentMeUrlUser(url=url, user_id=user_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(String(self.url))
        
        data.write(Int(self.user_id))
        
        return data.getvalue()
