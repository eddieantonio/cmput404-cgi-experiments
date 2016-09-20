#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright 2016 Eddie Antonio Santos <easantos@ualberta.ca>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
Roll my own "template system".
"""


from cgi import escape

__all__ = ['login_page', 'secret_page', 'after_login_incorrect']


def login_page():
    """
    Returns the HTML for the login page.
    """

    return _wrapper(r"""
    <h1> Welcome! </h1>

    <form method="POST" action="login.py">
        <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
        <label> <span>Password:</span> <input type="password" name="password"></label>

        <button type="submit"> Login! </button>
    </form>
    """)


def secret_page(username=None, password=None):
    """
    Returns the HTML for the page visited after the user has logged-in.
    """
    if username is None or password is None:
        raise ValueError("You need to pass both username and password!")

    return _wrapper("""
    <h1> Welcome, {username}! </h1>

    <p> <small> Pst! I know your password is
        <span class="spoilers"> {password}</span>.
        </small>
    </p>
    """.format(username=escape(username.capitalize()),
               password=escape(password)))


def after_login_incorrect():
    """
    Returns the HTML for the page when the login credentials were typed
    incorrectly.
    """
    return _wrapper(r"""
    <h1> Login incorrect :c </h1>

    <p> Incorrect username or password (hint: <span class="spoilers"> Check
        <code>secret.py</code>!</span>)
    <p> <a href="login.py"> Try again. </a>
    """)


def _wrapper(page):
    """
    Wraps some text in common HTML.
    """
    return ("""
    <!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, sans-serif;
                max-width: 24em;
                margin: auto;
                color: #333;
                background-color: #fdfdfd
            }

            .spoilers {
                color: rgba(0,0,0,0); border-bottom: 1px dashed #ccc
            }
            .spoilers:hover {
                transition: color 250ms;
                color: rgba(36, 36, 36, 1)
            }

            label {
                display: flex;
                flex-direction: row;
            }

            label > span {
                flex: 0;
            }

            label> input {
                flex: 1;
            }

            button {
                font-size: larger;
                float: right;
                margin-top: 6px;
            }
        </style>
    </head>
    <body>
    """ + page + """
    </body>
    </html>
    """)
