#直方图均衡化（即调整图像的对比度）,直方图即统计各像素点的频次
import cv2 as cv
import numpy as np
#全局直方图均衡化
def eaualHist_demo(image):
    #gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)    #opencv的直方图均衡化要基于单通道灰度图像
    #cv.namedWindow('input_image', cv.WINDOW_NORMAL)
    cv.imshow('input_image', image)
    dst = cv.equalizeHist(image)                #自动调整图像对比度，把图像变得更清晰
    #cv.namedWindow("eaualHist_demo", cv.WINDOW_NORMAL)
    cv.imshow("eaualHist_demo", dst)

#局部直方图均衡化
def clahe_demo(image):
    #gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    # clipLimit参数表示对比度的大小。
    # tileGridSize参数表示每次处理块的大小
    clahe = cv.createCLAHE(clipLimit=5.0, tileGridSize=(8,8))
    dst = clahe.apply(image)
    #cv.namedWindow("clahe_demo", cv.WINDOW_NORMAL)
    cv.imshow("clahe_demo", dst)
    np.save("loacl_histom.npy", dst)



g = np.load("gchannel.npy")

eaualHist_demo(g)
clahe_demo(g)

cv.waitKey(0)
cv.destroyAllWindows()