#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class FollowingTheTAsInstructionsError(Exception):
    def __init__(self):
        Exception.__init__(self, (
            "You must edit secret.py to change the username, password, "
            "and to delete this error!"
        ))

# Delete this line:
raise FollowingTheTAsInstructionsError

# Edit the following two lines:
username = "<pick a username here>"
password = "<pick a password here>"
