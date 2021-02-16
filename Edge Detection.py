#--------------------Sobel Filter------------------------

import numpy as np
import cv2
import matplotlib.pyplot as plt

img= cv2.imread('f16.jpg')
n,m,d=img.shape

# defining vertical and horizontal sobel filters
vertical_filter= [[-1,-2,-1],[0,0,0],[1,2,1]]
horizontal_filter=[[-1,0,1],[-2,0,2],[-1,0,1]]

#Apply vertical filter
vertical_edges_img= np.zeros([n,m])
for row in range(3,n-2):
   for col in range(3,m-2):
       pixel_box= img[row-1:row+2,col-1:col+2,0]
       transformed_pixels= vertical_filter*pixel_box
       vertical_score= transformed_pixels.sum()
       vertical_edges_img[row,col]=vertical_score*3
print(vertical_edges_img)


