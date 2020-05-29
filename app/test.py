import cv2
from datetime import datetime

now = datetime.now().time()

print("now =", now)
img = cv2.imread('img.jpg')
mask = cv2.imread('mask.png')
img_og = cv2.cvtColor(img, cv2.COLOR_RGB2Lab)
mask_og = cv2.cvtColor(mask, cv2.COLOR_RGBA2GRAY)
dst = img_og.copy()
cv2.xphoto.inpaint(img_og,mask_og, dst,0)
#dst = cv2.inpaint(img, mask_og, 3, cv2.INPAINT_TELEA)
dst_og = cv2.cvtColor(dst, cv2.COLOR_LAB2RGB)
cv2.imwrite('result.jpg', dst)
now = datetime.now().time()
print("End =", now)