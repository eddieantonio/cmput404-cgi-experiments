#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import cgi
import cgitb

import secret

# Print Python errors as HTML
cgitb.enable()

print "Content-Type: text/html"
print

method = os.getenv('REQUEST_METHOD')

login_page = r"""
<h1> Welcome! </h1>

<form method="POST" action="login.py">
    <label> Username: <input type="text" name="username"></label> <br>
    <label> Password: <input type="password" name="password"></label>

    <button type="submit"> Login! </button>
</form>
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

# http://stackoverflow.com/a/5285982/6626414

if method == 'GET':
    print login_page
elif method == 'POST':
    length = int(os.getenv('CONTENT_LENGTH', 0))
    post_data = sys.stdin.read(length)

    print post_data

    #form = cgi.FieldStorage()
    #print after_login.format(username=form.getfirst("username"),
    #                         password=form.getfirst("password"))
else:
    print ""
