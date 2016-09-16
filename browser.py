#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import cgitb
cgitb.enable()

user_agent = os.getenv('HTTP_USER_AGENT', '')

if 'curl' in user_agent:
    print "Content-Type: text/plain"
    print
    print  "You're using Curl!"
    exit(0)


print "Content-Type: text/html"
print
print "<h1> Hi! </h1>"


if 'Chrome' in user_agent:
    print "<p> I think you're using Chrome!"
elif 'Firefox' in user_agent:
    print "<p> Maybe you're using Firefox?"
else:
    print "<p> What are you even using?"
