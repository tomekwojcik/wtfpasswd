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
""""Tests for the fucking API."""

import unittest
from pwdgen.app import app
import json

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
    def test_json(self):
        response = self.app.get('/json')
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
        
        response = json.loads(self.app.get('/json').data)
        assert response['status'] == 'ok'
        assert response['fucking_password'] != None
        
        response = json.loads(self.app.get('/json?length=256').data)
        assert response['status'] == 'fucking_error'
        assert response['fucking_password'] == None
        
    def test_text(self):
        response = self.app.get('/text')
        assert response.headers['Content-Type'] == 'text/plain; charset=utf-8'
        assert response.data != 'Fucking Error'
        
        response = self.app.get('/text?length=256')
        assert response.data == 'Fucking Error'
        
        