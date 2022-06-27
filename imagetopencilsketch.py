#pip install numpy
#pip install imageio
#pip install opencv-python
#pip install image
#pip install scipy
import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "anuj.jpg"

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0,2989,0.5870,0.1140])                          #it is a 2-d array formula to convert image to gray scale

def dodge(front,back):
    final_sketch=front*255/(255-back)
    final_sketch[final_sketch>255]=255
    final_sketch[back==255]=255
    return final_sketch.astype('uint8')


ss = imageio.v2.imread(img)                 # to read given image
gray=rgb2gray(ss)                      # convert into black and while

i=255-gray                              #0,0,0 is gpr darkest color and 255,255,255 is for bright color
                                         #to convert it into blur imageio
blur=scipy.ndimage.filters.gaussian_filter(i,sigma=15)
                                           #sigma is the intensity of blurness of image
r=dodge(blur,gray)                         #this function will convert our image to sketch by taking two parameter
cv2.imwrite('anujsketch.png',r)
