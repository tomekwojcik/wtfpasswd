# -*- coding: utf-8 -*-
from flask import render_template, request, Response, jsonify, send_file
import json
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
    
def make_charset(parts):
    charset = ''
    for part in parts:
        try:
            charset += getattr(string, part)
        except AttributeError:
            raise RuntimeError('Options are fucking invalid')
            
    return charset
    
def read_request_args():
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
        template_vars['fucking_password'] = make_passwd(charset, template_vars['fucking_length'])
    except RuntimeError as error:
        template_vars['fucking_error'] = error.message
        template_vars['fucking_query_string'] = ''
        template_vars['fucking_password'] = ''
        
    return template_vars
    
@app.route('/', defaults=dict(format='html'))
@app.route('/<format>')
def index(format):
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