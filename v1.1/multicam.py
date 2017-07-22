#!/usr/bin/env python
"""v.1.0 """

import cv2
import numpy as np
import time

class Cam():
	_cam_register = {}
	folder = "/home/felipe/FFAK/v1.1/data/"
	date = (time.strftime("%m-%d-%Y"))

	def __init__(self, number, name, position):
		self.num = number
		self.nam = name
		self.pos = position
		self.title = "_" + str(self.num) + "_" + self.nam + "_" + self.pos
		self.address = self.folder + self.date + self.title
	
	def setCamera(self):
		camera = cv2.VideoCapture(self.num)
		self.ret,self.frame = camera.read()
		self._cam_register[self.num] = self.nam;
		cv2.imshow(self.title, self.frame)
		print("{} cameras registered.".format(len(self._cam_register)))

	def previewImage(self):
		print("preview camera")
	
	def saveImage(self):
		cv2.imwrite( self.address+".png", self.frame)
		print("image saved in the data folder")

	def destroyWindows(self):
		cv2.destroyAllWindows()

	def realeaseCam(self):
		self.camera.realease()

#cam0 = Cam(0,"webcam","top")
#cam0.setCamera()
#cam0.previewImage()
#cam0.saveImage()
cam1 = Cam(1,"l","l")
cam1.setCamera()
cam1.previewImage()
#cam1.saveImage()
#cam2 = Cam(2,"c","c")
#cam2.setCamera()
#cam2.previewImage()
#cam2.saveImage()
#cam3 = Cam(3,"r","r")
#cam3.setCamera()
#cam3.previewImage()
#cam3.saveImage()
#cam3.destroyWindows()

