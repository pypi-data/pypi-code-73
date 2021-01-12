#  Copyright (c) 2021. Davi Pereira dos Santos
#  This file is part of the lange project.
#  Please respect the license - more about this in the section (*) below.
#
#  lange is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  lange is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with lange.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is a crime and is unethical regarding the effort and
#  time spent here.
#  Relevant employers or funding agencies will be notified accordingly.

from lange.ap import AP
from lange.gp import GP


class APwithBrackets:
    def __getitem__(self, item):
        """Helper class to allow overriding square brackets.

        Import object 'ap' from module 'lange' to use it implicitly.

        Usage:
            >>> from lange import ap
            >>> (ap[0.6, 0.8, ..., 2])
            [0.6 0.8 .+. 2.0]
            >>> print(ap[0.6, 0.8, ..., 2])
            [0.6 0.8 1.0 1.2 1.4 1.6 1.8 2.0]
        """
        if isinstance(item, tuple):
            return AP(*item)
        else:
            return AP(item)


class GPwithBrackets:
    def __getitem__(self, item):
        """Helper class to allow overriding square brackets.

        Import object 'gp' from module 'lange' to use it implicitly.

        Usage:
            >>> from lange import gp
            >>> (gp[0.3, 0.6, ..., 2])
            [0.3 0.6 .*. 2.0]
            >>> print(gp[0.3, 0.6, ..., 2])
            [0.3 0.6 1.2]
        """
        if isinstance(item, tuple):
            return GP(*item)
        else:
            return GP(item)
