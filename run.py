# -*- coding: utf-8 -*-
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