import numpy as np
import cv2
import imutils

image=cv2.imread('f16.jpg')

print(image.shape)
#opencv expects M to be floating type and hence the np.float32() function
# Affine Transformation Matrix [1,0,tx],[0,1,ty]
# +ve tx to right and -ve tx to left
# +ve ty to down and -ve ty to up
# image.shape gives height,width,no of colours or channels
M=np.float32([[1,0,450],[0,1,-12]])
shifted_image1=cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))

#For cleaner code use Imutils
# imutils.translate(image,tx,ty) with the same convention as above
shifted_image2= imutils.translate(image,450,-100)

cv2.imshow('shifted_immge',shifted_image1)
cv2.waitKey(0)
cv2.destroyAllWindows()