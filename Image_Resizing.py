import numpy as np
import cv2
import imutils

image=cv2.imread('f16.jpg')
print(image.shape) # height,width,no of colours or channels

# # The ratio of new width to old width
# r= 100/image.shape[1]
# # New dimensions (width,height) i.e 100 width and r* old height
# dim= (100,int(image.shape[0]*r))

# dim is (new width and new height)
dim= (250,450)

# we have 3 interpolation methods in opencv
# 1) cv2.INTER_AREA - Used when we need to shrink an image
# 2) cv2.INTER_CUBIC- This is slow but efficient
# 3) cv2.INTER_LINEAR- Used when zooming is required. This is the default interpolation technique in opencv
resized=cv2.resize(image,dim,interpolation=cv2.INTER_LINEAR)
cv2.imshow('Resized',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()



#Cropping an Image
crop=image[100:300,200:400]
cv2.imshow('cropeed',crop)
cv2.waitKey(0)
cv2.destroyAllWindows()