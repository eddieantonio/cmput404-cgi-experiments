#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
A simple CGI server.

Usage:

    $ python cgi_server.py

Copyright 2016 Eddie Antonio Santos. Licensed under Apache 2.0.

Derived from Nick Zarczynski's blog post:
https://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/
"""


import BaseHTTPServer
import CGIHTTPServer
 
Server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
port = 8000
server_address = ("", port)
# Find CGI scripts in the current working directory.
handler.cgi_directories = ["/"]
 
httpd = Server(server_address, handler)
print("Server listening on http://{}:{}".format(
    httpd.server_name,
    httpd.server_port
))
httpd.serve_forever()
