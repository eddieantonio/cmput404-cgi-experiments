#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright (C) 2016  Eddie Antonio Santos <easantos@ualberta.ca>
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/>.


import os
import sys
import cgi
import cgitb
import hashlib

# Local imports:
import secret
from templates import login_page, secret_page, after_login_incorrect

# Print Python errors as HTML
cgitb.enable()


# Generate the cookie for the only logged-in user.
cookie = hashlib.sha224(secret.username + ':' + secret.password).hexdigest()

# Figure out the request method: GET? POST? Other?
method = os.getenv('REQUEST_METHOD')

print "Content-Type: text/html"

if method == 'GET':
    # Parse the cookie (if there is one).
    cookie_header = os.getenv('HTTP_COOKIE', '') or '='
    _, login_cookie = cookie_header.split('=')

    if login_cookie == cookie:
        # The user is logged-in.
        print
        print secret_page(username=secret.username,
                          password=secret.password)
    else:
        # Not logged in; show the login page.
        print
        print login_page()

elif method == 'POST':
    # Use CGI utils to parse things from the HTTP response.
    form = cgi.FieldStorage()
    username = form.getfirst("username")
    password = form.getfirst("password")

    if username == secret.username and password == secret.password:
        # Log the user in by setting the cookie.
        print "Set-Cookie:", "auth=" + cookie
        print
        print secret_page(username=username,
                          password=password)
    else:
        # Credentials incorrect,
        print
        print after_login_incorrect()
else:
    print "Status: 405 Method not allowed"
    print
