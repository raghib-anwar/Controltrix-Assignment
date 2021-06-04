import cv2
import numpy as np
img=cv2.imread("Plum.bmp")
imgedge=cv2.Canny(img,100,100)
cv2.imshow("Edgy Plum",imgedge)
cv2.waitKey(0)