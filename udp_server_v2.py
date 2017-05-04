import socket,threading,time,traceback,sys
import smtplib


host = ""
port = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
s.bind((host,port))

file = open("smart_tray.txt","wb")

while 1:
	try:
		message,address = s.recvfrom(4096)
		message=message[41:67]
		y = message[14:18]
		

		if float(y) > 0.08:
			localtime = time.asctime(time.localtime(time.time()))
			print " you only have half eggs " + localtime
			print "coordinate: " + y
			file.write("running out of eggs" + localtime)
			sys.exit(0)
		
		
	except(KeyboardInterrupt,SystemExit):
		raise
	except:
		traceback.print_exc()

