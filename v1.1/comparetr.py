#!/usr/bin/env python
"""v.1.0 """

import cv2
import numpy as np

import sys

from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average


def compare_images(img1, img2):
    img1 = normalize(img1)
    img2 = normalize(img2)
    print("img1")
    print(img1)
    print("img2")
    print(img2)
    diff = img1 - img2
    m_norm = sum(abs(diff))
    z_norm = norm(diff.ravel(), 0)
    return (m_norm, z_norm)

def to_grayscale(arr):
    if len(arr.shape) == 3:
        return average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr

def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng


file1, file2 = sys.argv[1:1+2]
#img1 = to_grayscale(imread(file1).astype("uint8"))
#img2 = to_grayscale(imread(file2).astype("uint8"))
#image1 = cv2.imread("/home/felipe/ffak2.jpg")
#image2 = cv2.imread("/home/felipe/ffak1.jpg")
image1 = cv2.imread(file1)
image2 = cv2.imread(file2)
imagegray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#image1 = cv2.imread("/home/felipe/foot_for_a_king_test_compare_images_1_version_1_day_1/ffak2.jpg")
#image2 = cv2.imread("/home/felipe/foot_for_a_king_test_compare_images_1_version_1_day_1/ffak1.jpg")
#n_m, n_0 = compare_images(img1, img2)
#print " per pixel:", n_m/img2.size
#print " per pixel:", n_0*1.0/img2.size


#diff = cv2.subtract(image1, image2)
diff = cv2.absdiff(image1, image2)

result = not np.any(diff)
#result = np.any(diff)

#cv2.imwrite("result21b.jpg", diff)
#ims = cv2.resize(diff, (1000, 740))
ims1 = cv2.resize(image1, (400, 240))
imsg = cv2.cvtColor(ims1, cv2.COLOR_BGR2GRAY)
ims2 = cv2.resize(image2, (400, 240))
ims3 = cv2.resize(diff, (400, 240))
vis = np.concatenate((ims1, ims2, ims3), axis=1)
cv2.imwrite("result_f.jpg", ims3)
cv2.imshow("result_f.jpg",vis)
cv2.waitKey(0)



