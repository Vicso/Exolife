#!/usr/python2.7.12
#-*-coding:Latin-1 -*
from PIL import Image
import numpy as np
from PIL import ImageFilter

def normalisation():

	img = Image.open('MissionB2.pbm')
	mat = np.array(img)

	x = np.amax(mat)
	y = np.amin(mat)

	mat -= y
	mat *= 255/(x-y)

	img = Image.fromarray(mat.astype('uint8'))
	img.show()

normalisation()