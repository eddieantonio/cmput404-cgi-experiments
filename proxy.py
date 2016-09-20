#!/usr/bin/env python

# Copyright 2016 Joshua Charles Campbell, Eddie Antonio Santos
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

import socket
import os

# Change this to change the proxy's listen port.
PORT = 12345
# Change this to change the hostname and port to proxy to.
PROXY_TO = ("localhost", 8000)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.bind(("0.0.0.0", PORT))
clientSocket.listen(5)
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    while True:

        (incomingSocket, address) = clientSocket.accept()
        print "we got a connection from %s!" % (str(address))

        pid = os.fork()
        if (pid == 0): # we must be the child (clone) process, so we will handle proxying for this client


            googleSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            googleSocket.connect(PROXY_TO)

            incomingSocket.setblocking(0)
            googleSocket.setblocking(0)

            while True:
                # This half of the loop forwards from
                # client to google
                skip = False
                try:
                    part = incomingSocket.recv(1024)
                except socket.error, exception:
                    if exception.errno == 11:
                        skip = True
                    else:
                        raise
                if not skip:
                    if (len(part) > 0):
                            print " > " + part
                            googleSocket.sendall(part)
                    else: # part will be "" when the connection is done
                        exit(0)

                # This half of the loop forwards from
                # google to the client
                skip = False
                try:
                    part = googleSocket.recv(1024)
                except socket.error, exception:
                    if exception.errno == 11:
                        skip = True
                    else:
                        raise
                if not skip:
                    if (len(part) > 0):
                            print " < " + part
                            incomingSocket.sendall(part)
                    else: # part will be "" when the connection is done
                        exit(0)
finally:
    clientSocket.close()