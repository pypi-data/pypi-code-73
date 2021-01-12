#  Copyright 2020-2021 Parakoopa and the SkyTemple Contributors
#
#  This file is part of SkyTemple.
#
#  SkyTemple is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  SkyTemple is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with SkyTemple.  If not, see <https://www.gnu.org/licenses/>.
from skytemple_files.common.types.data_handler import DataHandler
from skytemple_files.graphics.dpc.model import Dpc


class DbinAt4pxDpcHandler(DataHandler[Dpc]):

    @classmethod
    def deserialize(cls, data: bytes, **kwargs) -> Dpc:
        from skytemple_files.common.types.file_types import FileType
        at4px = FileType.AT4PX.deserialize(data)
        return FileType.DPC.deserialize(at4px.decompress())

    @classmethod
    def serialize(cls, data: Dpc, **kwargs) -> bytes:
        from skytemple_files.common.types.file_types import FileType
        serialized = FileType.DPC.serialize(data)
        return FileType.AT4PX.serialize(
            FileType.AT4PX.compress(serialized)
        )
