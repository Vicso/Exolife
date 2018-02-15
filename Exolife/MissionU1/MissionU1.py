#!/usr/python2.7.12
#-*-coding:Latin-1 -*
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps 
import numpy as np 
import matplotlib.pyplot as plt

img = Image.open('MissionU1.pbm')
#img.show()
img = img.filter(ImageFilter.FIND_EDGES())

for x in range (img.size[0]):
	for y in range (img.size [1]):
			pixel = img.getpixel((x, y))
			if pixel > 77.5:
				img.putpixel((x, y), 255)
			else :
				img.putpixel((x, y), 0)

img.save("u1Contour.pbm")
img = img.filter(ImageFilter.MaxFilter(3)) #remplace le pixel du milieu par la plus haute intensité
img.show()
img = img.filter(ImageFilter.SMOOTH) #lisse l'image
#img.show()
img = img.filter(ImageFilter.MinFilter(3)) #inverse max
#img.show()
img = img.filter(ImageFilter.DETAIL) #accentue les details
img.show()
img.save("finalimage.pbm")
#plt.hist(list(img.getdata()))
#plt.show()
