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
""""Tests for fucking password generator."""

import unittest
import re
from pwdgen.views import make_password, make_charset

class PwdgenTestCase(unittest.TestCase):
    _re_all_chars = re.compile(r"""^[a-zA-Z0-9!"#$%&\\'()*+,-\.\/:;<=>?@\[\]^_`{|}~]+?$""")
    _re_letters = re.compile(r"""^[a-zA-Z]+?$""")
    _re_digits = re.compile(r"""^[0-9]+?$""")
    _re_punctuation = re.compile(r"""^[!"#$%&\\'()*+,-\.\/:;<=>?@\[\]^_`{|}~]+?$""")
    
    all_chars = make_charset([
        'letters', 'digits', 'punctuation'
    ])
    letters = make_charset([ 'letters' ])
    digits = make_charset([ 'digits' ])
    punctuation = make_charset([ 'punctuation' ])
    
    def test_make_password(self):
        assert make_password() != make_password()
        assert len(make_password()) == 8
        assert make_password(charset='') == None
        assert make_password(length=0) == None
        assert make_password(length=256) == None
        
        all_chars_password = make_password(self.all_chars)
        assert self._re_all_chars.match(all_chars_password).span()[1] == len(all_chars_password)
        
        letters_password = make_password(self.letters)
        assert self._re_letters.match(letters_password).span()[1] == len(letters_password)
        
        digits_password = make_password(self.digits)
        assert self._re_digits.match(digits_password).span()[1] == len(digits_password)
        
        punctuation_password = make_password(self.punctuation)
        assert self._re_punctuation.match(punctuation_password).span()[1] == len(punctuation_password)
        
    def test_make_charset(self):
        assert self._re_all_chars.match(self.all_chars).span()[1] == len(self.all_chars)
        assert self._re_letters.match(self.letters).span()[1] == len(self.letters)
        assert self._re_digits.match(self.digits).span()[1] == len(self.digits)
        assert self._re_punctuation.match(self.punctuation).span()[1] == len(self.punctuation)