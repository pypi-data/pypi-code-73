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

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SentCode = Union[raw.types.auth.SentCode]


# noinspection PyRedeclaration
class SentCode:  # type: ignore
    """This base type has 1 constructor available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`auth.SentCode <pyrogram.raw.types.auth.SentCode>`

    See Also:
        This object can be returned by 5 methods:

        .. hlist::
            :columns: 2

            - :obj:`auth.SendCode <pyrogram.raw.functions.auth.SendCode>`
            - :obj:`auth.ResendCode <pyrogram.raw.functions.auth.ResendCode>`
            - :obj:`account.SendChangePhoneCode <pyrogram.raw.functions.account.SendChangePhoneCode>`
            - :obj:`account.SendConfirmPhoneCode <pyrogram.raw.functions.account.SendConfirmPhoneCode>`
            - :obj:`account.SendVerifyPhoneCode <pyrogram.raw.functions.account.SendVerifyPhoneCode>`
    """

    QUALNAME = "pyrogram.raw.base.auth.SentCode"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/sent-code")
