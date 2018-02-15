#!/usr/python2.7.12
#-*-coding:Latin-1 -*
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps 
import numpy as np 
import matplotlib.pyplot as plt

img = Image.open('MissionU2.pbm')
#img.show()
img = img.filter(ImageFilter.FIND_EDGES())

for x in range (img.size[0]):
	for y in range (img.size [1]):
			pixel = img.getpixel((x, y))
			if pixel > 175:
				img.putpixel((x, y), 255)
			else :
				img.putpixel((x, y), 0)

img.save("u2Contour.pbm")
img.show()
#img = img.filter(ImageFilter.SMOOTH_MORE) #remplace le pixel du milieu par la plus haute intensité

