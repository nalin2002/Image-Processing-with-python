import numpy as np
import cv2
import imutils
import argparse
# Extracting ROI
image=cv2.imread('f16.jpg')
image_grayscale= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # image in grayscale
cv2.imshow('gray',image_grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()

im1=cv2.GaussianBlur(image_grayscale,(3,3),0)
cv2.imshow('gray',im1)
cv2.waitKey(0)
cv2.destroyAllWindows()

im2=cv2.Canny(im1,20,100)
cv2.imshow('gray',im2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cnts = cv2.findContours(im2.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cv2.imshow('gray',im2)
cv2.waitKey(0)
cv2.destroyAllWindows()

if len(cnts)>0:
    c = max(cnts, key=cv2.contourArea)
    mask = np.zeros(image_grayscale.shape, dtype="uint8")

    cv2.drawContours(mask, [c], -1, 255, -1)

    (x, y, w, h) = cv2.boundingRect(c)
    imageROI = image[y:y + h, x:x + w]
    cv2.imshow('mask', imageROI)
    cv2.waitKey(0)
    maskROI = mask[y:y + h, x:x + w]
    cv2.imshow('mask', maskROI)
    cv2.waitKey(0)
    imageROI = cv2.bitwise_and(imageROI, imageROI,mask=maskROI)

# Rotating the ROI
for angle in np.arange(0,360,15):
    rotated=imutils.rotate(image,angle)
    cv2.imshow('Rotated(Problematic)',rotated)
    cv2.waitKey(0)

cv2.destroyAllWindows()
for angle in np.arange(0,360,15):
    rotated=imutils.rotate_bound(image,angle)
    cv2.imshow('Rotated Proper',rotated)
    cv2.waitKey(0)

cv2.destroyAllWindows()

#Another Method for Rotating
h,w= image.shape[:2]
center=(w/2,h/2) # if rotation wrt to any arbitary point then assign it to center here

angle=180 # the angle by which the image to be rotated
M= cv2.getRotationMatrix2D(center,angle,1) # 1 is the scaling factor . if 0.5 then image is halved
image_rotated=cv2.warpAffine(image,M,(w,h))
cv2.imshow('Rotated Image',image_rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

