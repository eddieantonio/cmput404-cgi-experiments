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
import errno

# Change this to change the proxy's listen port.
PORT = 12345
# Change this to change the hostname and port to proxy to.
PROXY_TO = ("localhost", 8000)

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.bind(("0.0.0.0", PORT))
listen_socket.listen(5)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print "Proxy listening on localhost:" + str(PORT) + "/"

try:
    while True:
        client_socket, address = listen_socket.accept()
        print "we got a connection from %s!" % (str(address))

        pid = os.fork()
        if (pid == 0):
            # we must be the child (clone) process, so we will handle proxying
            # for this client

            remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_socket.connect(PROXY_TO)

            client_socket.setblocking(0)
            remote_socket.setblocking(0)

            while True:
                # This half of the loop forwards from
                # client to google
                skip = False
                try:
                    part = client_socket.recv(1024)
                except socket.error, exception:
                    if exception.errno == errno.EAGAIN:
                        skip = True
                    else:
                        raise
                if not skip:
                    if (len(part) > 0):
                            print " > " + part
                            remote_socket.sendall(part)
                    else:
                        # part will be "" when the connection is done
                        print "exiting..."
                        client_socket.shutdown(socket.SHUT_RDWR)
                        client_socket.close()
                        remote_socket.shutdown(socket.SHUT_RDWR)
                        remote_socket.close()
                        exit(0)

                # This half of the loop forwards from the remote host to the
                # client
                skip = False
                try:
                    part = remote_socket.recv(1024)
                except socket.error, exception:
                    if exception.errno == errno.EAGAIN:
                        skip = True
                    else:
                        raise
                if not skip:
                    if (len(part) > 0):
                            print " < " + part
                            client_socket.sendall(part)
                    else:
                        # part will be "" when the connection is done
                        print "exiting..."
                        client_socket.shutdown(socket.SHUT_RDWR)
                        client_socket.close()
                        remote_socket.shutdown(socket.SHUT_RDWR)
                        remote_socket.close()
                        exit(0)

finally:
    listen_socket.close()
