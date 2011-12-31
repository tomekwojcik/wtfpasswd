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
"""View functions."""

from flask import render_template, request, Response, jsonify, send_file
import json
from pwdgen.app import app
from urllib import urlencode
import random, string

DEFAULT_CHARSET = string.ascii_letters + string.digits + string.punctuation

def make_password(charset=None, length=8):
    """Fucking password generator.
    
    Returns a string containing `length` random chars from `charset` string.
    Seting `charset` to None will force use of DEFAULT_CHARSET.
    Returns None if `charset` is empty or `length` is bigger than charset len.
    """
    if charset == None or isinstance(charset, str) == False:
        charset = DEFAULT_CHARSET
    else:
        try:
            charset = charset.encode('ascii')
        except:
            charset = DEFAULT_CHARSET
            
    try:
        assert len(charset) > 0
        assert int(length) > 0 and int(length) < len(charset)
    except:
        return None
            
    return ''.join(random.sample(charset, int(length)))
    
def make_charset(parts):
    """Creates charset string from `parts` list.
    
    Valid parts are names of constants from `string` module.
    Returns string or None."""
    charset = ''
    for part in parts:
        try:
            charset += getattr(string, part)
        except AttributeError:
            return None
            
    return charset
    
def read_request_args():
    """Reads request args (aka query string), if any and reacts accordingly.
    
    Returns a dictionary of values to be passed to template."""
    template_vars = {
        'fucking_password': '',
        'show_fucking_options': False,
        'fucking_error': None,
        'fucking_checkboxes': set([
            'letters', 'digits', 'punctuation'
        ]),
        'fucking_length': 8,
        'fucking_query_string': ''
    }
    
    if len(request.args) > 0:
        checkboxes = set()
        try:
            assert request.args['letters'] == 'yes'
        except:
            pass
        else:
            checkboxes.add('letters')
            
        try:
            assert request.args['digits'] == 'yes'
        except:
            pass
        else:
            checkboxes.add('digits')
            
        try:
            assert request.args['punctuation'] == 'yes'
        except:
            pass
        else:
            checkboxes.add('punctuation')
        
        if len(checkboxes) > 0:
            template_vars['fucking_checkboxes'] = checkboxes
        
        try:
            assert request.args.get('length') != None
        except:
            pass
        else:
            template_vars['fucking_length'] = request.args.get('length')
        
        template_vars['fucking_query_string'] = '?' + urlencode(request.args)
        template_vars['show_fucking_options'] = True
    
    try:    
        charset = make_charset(template_vars['fucking_checkboxes'])
        assert charset != None
        fucking_password = make_password(charset, template_vars['fucking_length'])
        assert fucking_password != None
    except AssertionError:
        template_vars['fucking_error'] = 'Options are fucking invalid'
        template_vars['fucking_query_string'] = ''
        template_vars['fucking_password'] = ''
    else:
        template_vars['fucking_password'] = fucking_password
        
    return template_vars
    
@app.route('/', defaults=dict(format='html'))
@app.route('/<format>')
def index(format):
    """Fucking home page."""
    template_vars = read_request_args()
            
    if format == 'json':
        response_args = {
            'response': '',
            'status': 200,
            'content_type': 'application/json; charset=utf-8'
        }
        
        response_data = {
            'status': 'ok',
            'fucking_password': template_vars['fucking_password']
        }
        
        if template_vars['fucking_error'] != None:
            response_args['status'] = 400
            response_data['status'] = 'fucking_error'
            response_data['fucking_password'] = None
            
        response_args['response'] = json.dumps(response_data)
        return Response(**response_args)
    elif format == 'text':
        response_args = {
            'response': template_vars['fucking_password'],
            'status': 200,
            'content_type': 'text/plain; charset=utf-8'
        }
        
        if template_vars['fucking_error'] != None:
            response_args['status'] = 400
            response_args['response'] = 'Fucking Error'
        
        return Response(**response_args)
    else:
        return render_template('index.html', **template_vars)