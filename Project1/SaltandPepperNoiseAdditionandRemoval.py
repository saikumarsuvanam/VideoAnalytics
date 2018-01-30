import numpy as np
import random
import median
import cv2

"""
Arguments:
Adds salt and pepper noise and detect the image
"""

#p is the percentage of an image that is corrupted (default 5% or 0.05), so sp = 20% = 0.2 means that 1 in 5 pixels are corrupted:
def sp_noise(src,percent):
    noisedImage = src.copy()
    for i in range(src.shape[0]):
        for j in range(src.shape[1]):
            value = random.random()
            if value > 1-percent:
                noisedImage[i][j] = 255
            elif value < percent:
                noisedImage[i][j] = 0
            
    return noisedImage


def medianFilter(noisedImage):
    filteredImage = noisedImage.copy()
    R=[]*9
    B=[]*9
    G=[]*9
    neighbours=[noisedImage[0,0]]*9
    for y in range(1,noisedImage.shape[0]-1):
        for x in range(1,noisedImage.shape[1]-1):
            neighbours[0] = noisedImage[y-1,x-1]
            neighbours[1] = noisedImage[y,x-1]
            neighbours[2] = noisedImage[y+1,x-1]
            neighbours[3] = noisedImage[y-1,x]
            neighbours[4] = noisedImage[y,x]
            neighbours[5] = noisedImage[y+1,x]
            neighbours[6] = noisedImage[y-1,x+1]
            neighbours[7] = noisedImage[y,x+1]
            neighbours[8] = noisedImage[y+1,x+1]
            for k in range(0,9):
                   B.append(neighbours[k][0])
                   G.append(neighbours[k][1])
                   R.append(neighbours[k][2])
            B.sort()
            G.sort()
            R.sort()
            filteredImage[y,x]=[B[4],G[4],R[4]]
            del R[:]
            del G[:]
            del B[:]
    return filteredImage

if __name__ == '__main__' :
    """
    test the program using sample image file
    """
    imgFile = cv2.imread('messi5.jpg',1)
    noise_img = sp_noise(imgFile,0.05)
    cv2.imwrite("noiseImage.png",noise_img)
    fin=medianFilter(noise_img)
    cv2.imwrite('filteredImage.png',fin)


