#!/usr/python2.7.12
#-*-coding:Latin-1 -*
from PIL import Image
import numpy as np
from PIL import ImageFilter
from PIL import ImageOps 
import matplotlib.pyplot as plt 

def normalisation():

	img = Image.open('MissionB1.pbm') 
	mat = np.array(img)

	x = np.amax(mat)
	y = np.amin(mat)

	mat -= y
	mat *= 290/(x-y)  #290 pour un intervalle plus grand =  plus clair
	img = Image.fromarray(mat.astype('uint8'))
	img.save("image normalisée.pbm")
	img.show()

normalisation()

def egalisation():
	img = Image.open('MissionB1.pbm') 
	imgegal = ImageOps.equalize(img)

	imgegal.save("image égalisée.pbm")
	imgegal.show()

egalisation()
