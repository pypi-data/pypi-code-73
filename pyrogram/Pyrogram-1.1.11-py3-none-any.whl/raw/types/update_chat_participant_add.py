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


class UpdateChatParticipantAdd(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``122``
        - ID: ``0xea4b0e5c``

    Parameters:
        chat_id: ``int`` ``32-bit``
        user_id: ``int`` ``32-bit``
        inviter_id: ``int`` ``32-bit``
        date: ``int`` ``32-bit``
        version: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["chat_id", "user_id", "inviter_id", "date", "version"]

    ID = 0xea4b0e5c
    QUALNAME = "types.UpdateChatParticipantAdd"

    def __init__(self, *, chat_id: int, user_id: int, inviter_id: int, date: int, version: int) -> None:
        self.chat_id = chat_id  # int
        self.user_id = user_id  # int
        self.inviter_id = inviter_id  # int
        self.date = date  # int
        self.version = version  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateChatParticipantAdd":
        # No flags
        
        chat_id = Int.read(data)
        
        user_id = Int.read(data)
        
        inviter_id = Int.read(data)
        
        date = Int.read(data)
        
        version = Int.read(data)
        
        return UpdateChatParticipantAdd(chat_id=chat_id, user_id=user_id, inviter_id=inviter_id, date=date, version=version)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(Int(self.chat_id))
        
        data.write(Int(self.user_id))
        
        data.write(Int(self.inviter_id))
        
        data.write(Int(self.date))
        
        data.write(Int(self.version))
        
        return data.getvalue()
