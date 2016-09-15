#! /usr/bin/env python

import socket

# internet socket to communicate with other computer
# want a TCP socket (in TCP, can just send back and forth
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# C programming in python
# make connection
clientSocket.connect(("www.google.com", 80))

clientSocket.sendall("GET / HTTP/1.0\r\n\r\n")

while True:
  # in c, tell system how big to allocate 
  part = clientSocket.recv(1024)
  if (len(part)>0):
    print part
  else:
    # part will be "" when the connection is done
    exit(0)

