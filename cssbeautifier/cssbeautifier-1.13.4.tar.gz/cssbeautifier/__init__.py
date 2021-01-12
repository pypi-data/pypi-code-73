#
# The MIT License (MIT)

# Copyright (c) 2007-2018 Einar Lielmanis, Liam Newman, and contributors.

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys


def default_options():
    _main = __import__("cssbeautifier", globals(), locals(), ["_main"])._main
    return _main.default_options()


def beautify(string, opts=None):
    _main = __import__("cssbeautifier", globals(), locals(), ["_main"])._main
    return _main.beautify(string, opts)


def beautify_file(file_name, opts=None):
    _main = __import__("cssbeautifier", globals(), locals(), ["_main"])._main
    return _main.beautify_file(file, opts)


def usage(stream=sys.stdout):
    _main = __import__("cssbeautifier", globals(), locals(), ["_main"])._main
    return _main._sage(stream)


def main():
    _main = __import__("cssbeautifier", globals(), locals(), ["_main"])._main
    return _main.main()
