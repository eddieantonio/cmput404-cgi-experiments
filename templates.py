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

"""
Roll my own "template system".
"""


__all__ = ['login_page', 'secret_page']


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
    if username is None or password is None:
        raise ValueError("")

    return _wrapper("""
    <h1> Welcome, {username}! </h1>

    <p> <small> Pst! I know your password is
        <span class="spoilers"> {password}</span>.
        </small>
    </p>
    """.format(username, password))

    return css + template


# TODO: Convert these to functions.
normal_page = r"""
<h1> Hello, {username}! </h1>
"""

after_login = r"""
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
normal_page = r"""
<h1> Hello, {username}! </h1>
"""

after_login = r"""
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


def _wrapper(page):
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
