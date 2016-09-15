#! /usr/bin/env python

#client send to proxy, proxy send to server
#server send the feedback to proxy, proxy send to client

# demo of a simple one to build a proxy deal with only one website

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# listen on any address that i listen on computer
# listen a port higher than 1024
clientSocket.bind(("0.0.0.0",1600))
clientSocket.listen(5)
# solve the address is already in use problem
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)


(incomingSocket,address) = clientSocket.accept()
print "we got a connection from %s!" % (str(address))

googleSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# if change to ca, curl 127.0.0.1:1600 -H "Host: www.google.ca"
# it gonna fail we are waiting for curl, curl is waiting us
googleSocket.connect(("www.google.ca", 80))
googleSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

# tell system never hang on here to wait forever
# get a error
incomingSocket.setblocking(0)

while True:
  # this half of the loop forward from client to google
  skip = False
  try:
    part = incomingSocket.recv(1024)
  except socket.error, exception:
    if exception.errno == 11:
      skip = True
    else:
      raise
  if not skip: 
    if (len(part)>0):
      print " > " + part
      googleSocket.sendall(part)
    else:
      exit(0)

  skip = False
  try:
    part = googleSocket.recv(1024)
  except socket.error, exception:
    if exception.errno == 11:
      skip = True
    else:
      raise
  if not skip: 
  # this half of the loop forwards from google to the client
    if (len(part)>0):
      print " < " + part
      incomingSocket.sendall(part)
    else:
    # part will be "" when the connection is done
      exit(0)




