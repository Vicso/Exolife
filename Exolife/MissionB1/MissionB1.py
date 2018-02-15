#!/usr/python2.7.12
#-*-coding:Latin-1 -*
from PIL import Image
import numpy as np
from PIL import ImageFilter

def normalisation():

	img = Image.open('MissionB1.pbm')
	mat = np.array(img)

	x = np.amax(mat)
	y = np.amin(mat)

	mat -= y
	mat *= 290/(x-y)  #290 pour un intervalle plus grand =  plus clair
	img = Image.fromarray(mat.astype('uint8'))
	img.show()

normalisation()


