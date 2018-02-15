#!/usr/python2.7.12
#-*-coding:Latin-1 -*
from PIL import Image
import numpy as np

img = Image.open('MissionA1.pbm')
mat = np.array(img)
nbc, nbl = mat.shape
Vmax = np.amax(mat)
print Vmax
x,y = map(lambda x: x[0],np.where(mat==Vmax))

print "coordonnées %s = (%s,%s) " % (Vmax,x,y)