#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import cgi
import cgitb

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

# http://stackoverflow.com/a/5285982/6626414

if method == 'GET':
    print login_page
elif method == 'POST':
    form = cgi.FieldStorage()
    print "Ha ha, your password is", form.getfirst('password', '')
else:
    print ""
