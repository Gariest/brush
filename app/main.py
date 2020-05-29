import time
import cv2
import sys
import time
import json
#from gevent import getcurrent, wait
from uuid import uuid4
import datetime

img = cv2.imread('img.jpg')
mask = cv2.imread('mask_inverse.png')
img_og = cv2.cvtColor(img, cv2.COLOR_RGB2Lab)
mask_og = cv2.cvtColor(mask, cv2.COLOR_RGBA2GRAY)
dst = img_og.copy()
print('HUH')
cv2.xphoto.inpaint(img_og,mask_og, dst,0)
#dst = cv2.inpaint(img, mask_og, 3, cv2.INPAINT_TELEA)
dst_og = cv2.cvtColor(dst, cv2.COLOR_LAB2RGB)
print('END')
cv2.imwrite('result.jpg', dst_og)