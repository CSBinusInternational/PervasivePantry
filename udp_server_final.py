#!/usr/bin/python

import socket,threading,datetime,traceback,sys
import smtplib


host = ""
port = 5555
today = datetime.datetime.now()

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
s.bind((host,port))

file = open("smart_tray.txt","a")

note_log = str(today.day) +"-" + str(today.month) + "-" + str(today.day) + " = " + str(today.hour) + ":" + str(today.minute) + ":" + str(today.second)
while 1:
	try:
		message,address = s.recvfrom(4096)
		message=message[41:67]
		y = message[14:18]
		

		if float(y) > 0.1:
			print "Hey! Your stock is going to run out soon." + note_log
			print "latitude: " + y

                        email = #youremailpantry
                        password = #yourpasswordpantry
                        email_to = #youremail

                        server = smtplib.SMTP("smtp.gmail.com",587)
                        server.starttls()
                        server.login(email,password)

                        body = "you low running on stick, so fill me semour"

                        server.sendmail(email,email_to,body)
                        server.quit()

			file.write("\n Out of stocks. Please re-stock." + note_log)
			sys.exit(0)
		
		
	except(KeyboardInterrupt,SystemExit):
		raise
	except:
		traceback.print_exc()

