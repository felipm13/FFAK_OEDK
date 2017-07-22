import cv2
import numpy as np

import sys

from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average


def compare_images(img1, img2):
    # normalize to compensate for exposure difference
    img1 = normalize(img1)
    img2 = normalize(img2)
    print("img1")
    print(img1)
    print("img2")
    print(img2)
    # calculate the difference and its norms
    diff = img1 - img2  # elementwise for scipy arrays
    m_norm = sum(abs(diff))  # Manhattan norm
    z_norm = norm(diff.ravel(), 0)  # Zero norm
    return (m_norm, z_norm)

def to_grayscale(arr):
    "If arr is a color image (3D array), convert it to grayscale (2D array)."
    if len(arr.shape) == 3:
        return average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr

def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng


file1, file2 = sys.argv[1:1+2]
img1 = to_grayscale(imread(file1).astype("uint8"))
img2 = to_grayscale(imread(file2).astype("uint8"))
image1 = cv2.imread("/home/felipe/ffak2.jpg")
image2 = cv2.imread("/home/felipe/ffak1.jpg")
n_m, n_0 = compare_images(img1, img2)
print " per pixel:", n_m/img2.size
print " per pixel:", n_0*1.0/img2.size


#diff = cv2.subtract(image1, image2)
diff = cv2.absdiff(image1, image2)

result = not np.any(diff)

cv2.imwrite("result21b.jpg", diff)
ims = cv2.resize(diff, (1000, 740))
ims1 = cv2.resize(image1, (400, 240))
ims2 = cv2.resize(image2, (400, 240))
ims3 = cv2.resize(diff, (400, 240))
vis = np.concatenate((ims1, ims2, ims3), axis=1)
cv2.imshow("result_f.jpg",vis)
cv2.waitKey(0)



