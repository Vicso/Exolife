#!/usr/python2.7.12
#-*-coding:Latin-1 -*
from PIL import Image
import numpy as np
from PIL import ImageFilter
img1 = Image.open('Jupiter1.pbm')
img1 = img1.filter(ImageFilter.MedianFilter(3))
img2 = Image.open('Jupiter2.pbm')
img2 = img2.filter(ImageFilter.MedianFilter(3))

img1.show()
img2.show()
