#!/usr/bin/env python
# encoding: utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext

from django.utils.hashcompat import sha_constructor

import time
import settings

def go_permission_error(request, msg=None):
    """
    return permisson error page

    """
    return render_to_response('permission_error.html', {
            'error_msg': msg or u'权限错误',
            }, context_instance=RequestContext(request))

def go_error(request, msg=None):
    """
    return normal error page

    """
    return render_to_response('error.html', {
            'error_msg': msg or u'内部错误',
            }, context_instance=RequestContext(request))

def list_to_string(l):
    """
    return string of a list

    """
    tmp_str = ''
    for e in l[:-1]:
        tmp_str = tmp_str + e + ', '
    tmp_str = tmp_str + l[-1]
    
    return tmp_str

def get_httpserver_root():
    """
    Get seafile http server address and port from settings.py,
    and cut out last '/'

    """
    if settings.HTTP_SERVER_ROOT[-1] == '/':
        http_server_root = settings.HTTP_SERVER_ROOT[:-1]
    else:
        http_server_root = settings.HTTP_SERVER_ROOT
    return http_server_root

def get_ccnetapplet_root():
    """
    Get ccnet applet address and port from settings.py,
    and cut out last '/'

    """
    if settings.CCNET_APPLET_ROOT[-1] == '/':
        ccnet_applet_root = settings.CCNET_APPLET_ROOT[:-1]
    else:
        ccnet_applet_root = settings.CCNET_APPLET_ROOT
    return ccnet_applet_root

def gen_token():
    """
    Generate short token used for owner to access repo file

    """

    token = sha_constructor(settings.SECRET_KEY + unicode(time.time())).hexdigest()[::8]
    return token