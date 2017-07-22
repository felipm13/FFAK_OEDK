#!/usr/bin/env python
"""v.1.0 """

import smtplib

umail = "diabeticfootchecker@gmail.com"
upass = ""
pmail = "kyb1@rice.edu"
servre = smtplib.SMTP('smtp.gmail.com' , 587)
server.starttls()
server.login(umail, upass)

msg = "FFAK - TEST"

server.sendmail(umail,pmail,msg)
server.quit()
