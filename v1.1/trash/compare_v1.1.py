import cv2
import numpy as np
import sys
from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average

Class Image():
	def __init__(self, file1, file2):
		self.file1_add = file1
		self.file2_add = file2

	def toGrayScale(self, arr):
		if len(arr.shape) == 3:
			return average(arr, -1)
		else:
			return arr

	def normalize(self, arr):
		rng = arr.max()-arr.min()
		amin = arr.min()
		return (arr-amin)*255/rng

	def selectFiles():
		image1 = cv2.imread(self.file1_add)
		image2 = cv2.imread(self.file2_add)
		image1_gray = self.toGrayScale(imread(self.file1).astype("uint8"))
		image2_gray = self.toGrayScale(imread(self.file2).astype("uint8"))

	def convertFiles():

	def differenceFiles():

	def percentFiles():

	def resizeFiles():

	def saveFiles():

def __main__():
	file1, file2 = sys.argv[1:1+2]
    image = Image(file1, file2)	

