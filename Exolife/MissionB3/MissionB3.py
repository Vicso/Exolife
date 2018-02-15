#!/usr/python2.7.12
#-*-coding:Latin-1 -*
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 


img = Image.open('MissionB3.pbm')

mat = np.array(img) #matrice de l'image avec nuances de gris
#print mat
nbc = img.size[1]
#print nbc
nbl = img.size[0]
#print nbc
final = np.zeros((nbc,nbl)) #matrice image final initialisée a 0
zone1 = np.zeros((nbc,nbl)) #matrice zone 1 initialisée a 0
zone2 = np.zeros((nbc,nbl)) #matrice zone 2 initialisée a 0
zone3 = np.zeros((nbc,nbl)) #matrice zone 3 initialisée a 0
zone4 = np.zeros((nbc,nbl)) #matrice zone 4 initialisée a 0

i=0
j=0

while i<nbc:
    while j<nbl:
        if mat[i,j]<50:  #valeur pixels matrice de base inférieur a 50
            final[i,j]=0;   #mettre a jour la matrice de l'image final en nuance de gris
            zone1[i,j]=255;  #afficher en blanc toute les zone inférieur a 50
        elif 50<=mat[i,j]<127:  #valeur dans un intervl de pixel dans matrice de base
            final[i,j]=85;
            zone2[i,j]=255;
        elif 127<=mat[i,j]<230:
            final[i,j]=180;
            zone3[i,j]=255;
        else:
            final[i,j]=255;
            zone4[i,j]=255;  
        j+=1
    i+=1
    j=0

final = Image.fromarray(final.astype('uint8'))  #transformer la matrice final en une image en nuances de gris
zone1 = Image.fromarray(zone1.astype('uint8'))  #transforme la matrice zone1 en image en valeur binaires
zone2 = Image.fromarray(zone2.astype('uint8'))
zone3 = Image.fromarray(zone3.astype('uint8'))
zone4 = Image.fromarray(zone4.astype('uint8'))
final.show() #affiche l'image final
zone1.show() #affcihe l'image de la zone1   
zone2.show()
zone3.show()
zone4.show()

def plotHisto(d) :
    plt.bar( range(len(d)) , d.values(), align='center')
    plt.title('Histogram')
    plt.xlabel('Intensity')
    plt.ylabel('Number of pixels')
    plt.show()


def buildHisto(mat):
    unique, counts = np.unique(mat, return_counts = True)
    d = dict(zip(unique, counts))
    d.update( {i : 0 for i in range(256) if i not in d.keys()} )

    return d


img = Image.open('MissionB3.pbm').convert('L')
mat = np.array(img)
d = buildHisto(mat)
plotHisto(d)