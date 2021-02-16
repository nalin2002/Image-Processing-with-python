import cv2
import numpy as np

image_rgb= cv2.imread('f16.jpg')
image_grey=cv2.cvtColor(image_rgb,cv2.COLOR_BGR2GRAY)
template_rgb= cv2.imread('f16_template.jpg')
template_grey=cv2.cvtColor(template_rgb,cv2.COLOR_BGR2GRAY)

h,w= template_grey.shape[::]
res=cv2.matchTemplate(image_grey,template_grey,cv2.TM_SQDIFF)
print(res)
#Different methods available: ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
# 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
threshold = 23800000
loc = np.where( res <= threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(image_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)


cv2.imshow("Matched image", image_rgb)
cv2.waitKey()
cv2.destroyAllWindows()