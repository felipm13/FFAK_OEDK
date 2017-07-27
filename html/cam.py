#!/usr/bin/env python

import time
import os
import subprocess
import RPi.GPIO as GPIO
import csv
cams = subprocess.check_output('ls /dev/video* | wc -w', shell=True) #could be anything here.
num_cam = int(cams[0])

try:
    os.system('rm /var/www/html/data/lastExam.csv')

except:
    print("ok")

class Cam():
    _cam_register = {}
    folder_img = "/var/www/html/img/"
    folder_data = "/var/www/html/data/"
    date = (time.strftime("%m-%d-%Y"))
    date2 = (time.strftime("%m-%d-%Y-%H-%M-%S"))

    def __init__(self, number, name, position):
        self.num = number
        self.nam = name
        self.pos = position
        self.title = "_" + str(self.num) + "_" + self.nam + "_" + self.pos
        self.driver = '/dev/video' + str(self.num)
        self.address = self.folder_img +'cam'+ str(self.num) + self.date2 + '.jpg'
    
    def setCamera(self):
        self._cam_register[self.num] = self.nam;
        with open(self.folder_data + 'lastExam.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([self.driver, self.num, self.nam, self.pos, self.date, 'img/cam'+ str(self.num) + self.date2 + '.jpg'])
        with file(self.folder_data + 'historyExam.csv', 'r') as original: data = original.read()
        with open(self.folder_data + 'historyExam.csv', 'w') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([self.driver, self.num, self.nam, self.pos, self.date, 'img/cam'+ str(self.num) + self.date2 + '.jpg'])
        with file(self.folder_data + 'historyExam.csv', 'a') as modified: modified.write(data)

    def saveImage(self):
        os.system('fswebcam  -i 0 -d ' +  self.driver + ' --jpeg 85  --save ' + self.address+' --skip 8 --frames 1 -r 2560x1920 -s Contrast=95% -D 1 -s Gamma=90% --set brightness=55% --no-banner')


GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

GPIO.output(18, 1)

#for n in range(0, num_cam):
    #camera = Cam(n, "Camera " + str(n), "position")
    #camera.setCamera()
    #camera.saveImage()

camera1 = Cam(1, "Bottom", "position")
camera1.setCamera()
camera1.saveImage()
GPIO.output(18, 0)
camera2 = Cam(0, "Toe", "position")
camera2.setCamera()
camera2.saveImage()

