#!/usr/python2.7.12
#-*-coding:Latin-1 -*
from PIL import Image
import numpy as np

img = Image.open('MissionA3.pbm')
nbc = img.size[0]
nbl = img.size [1]

val=0

mat = np.array(img)

for l in range (nbl):
	for c in range(nbc):
		val=mat[l, c]
		if val<200:
			mat[l,c]=0
		else:
			mat[l,c]=255

img = Image.fromarray(mat.astype('uint8'))
img.show()
