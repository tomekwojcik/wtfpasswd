#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2011 by Tomasz Wójcik <labs@tomekwojcik.pl>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""Application wrapper.

Use this script to run an instance of the app.
"""

from optparse import OptionParser
from pwdgen.app import app
import logging
    
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-a', '--address', dest="address", help="address to bind to. Defaults to 127.0.0.1", action="store", default="127.0.0.1")
    parser.add_option('-p', '--port', dest="port", help="port to bind to. Defaults to 8888.", action="store", type="int", default=8888)
    parser.add_option('-d', '--debug', dest="debug", help="debugging?", action="store_true", default=False)
    options, args = parser.parse_args()
    
    app.run(host=options.address, port=options.port, debug=options.debug)