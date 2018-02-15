#!/usr/python2.7.12
#-*-coding:Latin-1 -*
from PIL import Image
import numpy as np

img = Image.open('MissionA2.pbm')
nbc = img.size[0]
nbl = img.size [1]
x=0
val=0
mat = np.array(img)

for l in range (nbl):
	for c in range(nbc):
		x+=1
		val+=mat[l, c]
#print val
#print x
f=val/x
#print f
vf=((f*50)/127)
print "Le pourcentage total de gaz présent sur cette image est de :",vf, "%"
