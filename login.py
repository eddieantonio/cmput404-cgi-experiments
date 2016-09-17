#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import cgi
import cgitb
import hashlib

import secret

cookie = hashlib.sha224(secret.username + ':' + secret.password).hexdigest()

# Print Python errors as HTML
cgitb.enable()

method = os.getenv('REQUEST_METHOD')

login_page = r"""
<h1> Welcome! </h1>

<form method="POST" action="login.py">
    <label> Username: <input type="text" name="username"></label> <br>
    <label> Password: <input type="password" name="password"></label>

    <button type="submit"> Login! </button>
</form>
"""

normal_page = r"""
<h1> Hello, {username}! </h1>
"""

after_login = r"""
<style>
    body {{
        color: #333;
        background-color: #fdfdfd
    }}
    .spoilers {{
        color: rgba(0,0,0,0); border-bottom: 1px dashed #ccc
    }}
    .spoilers:hover {{
        transition: color 250ms;
        color: rgba(36, 36, 36, 1)
    }}
</style>

<h1> Welcome, {username}! </h1>

<p> <small> Pst! I know your password is
    <span class="spoilers"> {password}</span>.
    </small>
</p>
"""

after_login_incorrect = r"""
<h1> Login incorrect! </h1>
<a href="login.py"> Try again. </a>
"""

# http://stackoverflow.com/a/5285982/6626414

print "Content-Type: text/html"

if method == 'GET':
    cookie_header = os.getenv('HTTP_COOKIE', '') or '='
    _, login_cookie = cookie_header.split('=')

    if login_cookie == cookie:
        print normal_page.format(username=secret.username)
    else:
        # Not logged in
        print
        print login_page

elif method == 'POST':
    form = cgi.FieldStorage()
    username = form.getfirst("username")
    password = form.getfirst("password") 

    if username == secret.username and password == secret.password:
        print "Set-Cookie:", "auth=" + cookie
        print
        print after_login.format(username=username, password=password)
    else:
        print
        print after_login_incorrect

else:
    print "Method not allowed"
