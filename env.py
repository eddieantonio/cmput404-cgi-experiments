#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import json

import urlparse

import cgitb
## This line enables CGI error reporting
cgitb.enable()

print "Content-Type: application/json"
print ""


qs = urlparse.parse_qs(os.getenv('QUERY_STRING'))

varnames = qs.get('var', [])

if len(varnames) == 1:
    var, = varnames
    print json.dumps(os.getenv(var))
else:
    #print json.dumps(qs)
    print json.dumps(dict(os.environ))

