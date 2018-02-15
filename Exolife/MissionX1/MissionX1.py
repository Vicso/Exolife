#!/usr/python2.7.12
#-*-coding:Latin-1 -*
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt 

myarray = np.fromfile('MissionX1.dat',dtype=float)

myarray.show()