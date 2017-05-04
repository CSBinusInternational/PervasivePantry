#!/usr/bin/python

import socket, traceback
host = '127.0.0.1'
port = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
s.bind((host,port))

while 1:
	try:
		message, address = s.recvfrom(2048)
		print address[0]
		print address[1]
		print message
	except (KeyboardInterrupt,SystemExit):
	raise
	except:
		traceback.print_exc()
