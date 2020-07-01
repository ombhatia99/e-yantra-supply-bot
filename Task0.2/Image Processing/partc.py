import numpy as np
import cv2
import os

i = cv2.imread('flowers.jpg')
img = np.array(i, dtype=np.float)
img /= 255.0
#pre-multiplication
a_channel = np.ones(img.shape, dtype=np.float)/2
image = img*a_channel
cv2.imwrite('..\Images\flowers_alpha.png',image)

cv2.imshow('img',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('..\Images\flowers_alpha.png',image)

