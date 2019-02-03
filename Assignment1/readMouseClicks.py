import matplotlib.pyplot as plt
import cv2
import numpy as np

im = cv2.imread("IMG_5455.JPG")

im_resized = cv2.resize(im, (5472, 3648), interpolation=cv2.INTER_LINEAR)
plt.imshow(cv2.cvtColor(im_resized, cv2.COLOR_BGR2RGB))
plt.show()
