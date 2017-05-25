#!/usr/bin/python

import smtplib

email = #yoursmarttrayemail
password = #yourpasswordsmarttray
email_to = #youremail

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(email,password)

body = "you low running on egg, so fill me semour"

server.sendmail(email,email_to,body)
server.quit()

