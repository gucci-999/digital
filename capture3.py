import numpy as np
from numpy.random import rand
from numpy import uint8, float32, float64, log, pi, sin, cos, abs, sqrt

import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from skimage.io import imread, imsave

import cv2
import os

a = os.listdir('c:\\Users\\yuki\\result')

meanR = np.zeros(200)
meanG = np.zeros(200)
meanB = np.zeros(200)

for i in np.arange(200):
    j = int(i)
    b = str(a[j])
    im = imread('/Users/yuki/result/' + b)
    imR = im[:,:,0];
    imG = im[:,:,1];
    imB = im[:,:,2];
    h,w = imR.shape

    for y in range(h):
        for x in range(w):
            meanR[j] += imR[y, x]
            meanG[j] += imG[y, x]
            meanB[j] += imB[y, x]

k = np.arange(200)

meanR /= h*w
meanG /= h*w
meanB /= h*w

plt.plot(k, meanR, "-r")
plt.plot(k, meanG, "-g")
plt.plot(k, meanB, "-b")
plt.xlabel("frame number", fontsize=10)
plt.ylabel("Brightness value", fontsize=10)
plt.savefig('/Users/yuki/Brightness.pdf')
plt.show()