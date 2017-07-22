import os
import time
import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

imgs = []

with open('data/lastExam.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        imgs.append(row[5])
    
msg = MIMEMultipart()
sender = 'diabeticfootchecker@gmail.com'
recipients = ['cjs11@rice.edu','cd37@rice.edu','lfs3@rice.edu','kyb1@rice.edu']

with open('settings.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        recipients.append(row[0])

date = (time.strftime("%m-%d-%Y"))
sub = 'Exam Results: ' + date
msg['Subject'] = sub
msg['From'] = sender
msg['To'] = ", ".join(recipients)

body = """
Dear User,
Attached below are the images from your last exam.


FFAK - TEAM
"""
text = MIMEText(body)

msg.attach(text)

for exam in imgs:
    img_data = open(exam, 'rb').read()
    image = MIMEImage(img_data, name=os.path.basename(exam))
    msg.attach(image)

s = smtplib.SMTP('smtp.gmail.com', '587')
s.ehlo()
s.starttls()
s.ehlo()
s.login(sender, '')
s.sendmail(sender, recipients, msg.as_string())
s.quit()
