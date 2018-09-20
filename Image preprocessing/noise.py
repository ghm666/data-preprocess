from numpy import *
import numpy as np
import cv2

def SaltAndPepper(src,percetage):
    SP_NoiseImg=src
    SP_NoiseNum=int(percetage*src.shape[0]*src.shape[1])
    for i in range(SP_NoiseNum):
        randX=random.random_integers(0,src.shape[0]-1)
        randY=random.random_integers(0,src.shape[1]-1)
        if random.random_integers(0,1)==0:
            SP_NoiseImg[randX,randY]=0
        else:
            SP_NoiseImg[randX,randY]=255
    return SP_NoiseImg

local_his = np.load("loacl_histom.npy")
cv2.imshow("clahe_demo", local_his)

SaltAndPepper_noiseImage = SaltAndPepper(local_his,0.1) #添加10%的椒盐噪声
cv2.imshow("Add_SaltAndPepperNoise Image",SaltAndPepper_noiseImage)
cv2.waitKey(0)
cv2.destroyAllWindows()