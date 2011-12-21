# -*- coding: utf-8 -*-
from flask import render_template, request
from pwdgen.app import app
from urllib import urlencode

import random, string

DEFAULT_CHARSET = string.ascii_letters + string.digits + string.punctuation

def make_passwd(charset=None, length=8):
    if charset == None or isinstance(charset, str) == False:
        charset = DEFAULT_CHARSET
    else:
        try:
            charset = charset.encode('ascii')
        except:
            charset = DEFAULT_CHARSET
            
    try:
        assert len(charset) > 0
        assert int(length) >= 0 and int(length) < len(charset)
    except:
        raise RuntimeError('Options are fucking invalid')
            
    return ''.join(random.sample(charset, int(length)))
    
@app.route('/', methods=[ 'GET', 'POST' ])
def index():
    template_vars = {
        'fucking_password': '',
        'show_fucking_options': False,
        'fucking_error': None,
        'fucking_checkboxes': [],
        'fucking_length': 8,
        'fucking_query_string': ''
    }
    
    if len(request.args) > 0:
        charset = ''
        try:
            assert request.args['letters'] == 'yes'
        except:
            pass
        else:
            template_vars['fucking_checkboxes'].append('letters')
            charset += string.ascii_letters
            
        try:
            assert request.args['digits'] == 'yes'
        except:
            pass
        else:
            template_vars['fucking_checkboxes'].append('digits')
            charset += string.digits
            
        try:
            assert request.args['punctuation'] == 'yes'
        except:
            pass
        else:
            template_vars['fucking_checkboxes'].append('punctuation')
            charset += string.punctuation
            
        template_vars['fucking_length'] = request.args.get('length', '')
        
        try:    
            template_vars['fucking_password'] = make_passwd(charset, request.args.get('length', None))
        except RuntimeError as error:
            template_vars['fucking_error'] = error.message
        else:
            template_vars['fucking_query_string'] = '?' + urlencode(request.args)
        
        template_vars['show_fucking_options'] = True
    else:
        template_vars['fucking_checkboxes'] = [ 'letters', 'digits', 'punctuation' ]
        template_vars['fucking_password'] = make_passwd()
            
    return render_template('index.html', **template_vars)