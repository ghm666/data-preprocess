#!/usr/bin/env python
# encoding: utf-8
#RGB通道的分离与保存

import numpy as np
import cv2

img = cv2.imread("BRVO1.jpg")
img = cv2.resize(img,(768,576))
cv2.imshow("Original", img)
b, g, r = cv2.split(img)
cv2.imshow("Blue", b)
cv2.imshow("Red", r)
cv2.imshow("Green", g)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 也可以单独返回其中一个通道
# b = cv2.split(img)[0]  # B通道
# g = cv2.split(img)[1]  # G通道
# r = cv2.split(img)[2]  # R通道

# 使用Numpy 数组来实现图像通道分离
# 创建3个跟图像一样大小的矩阵，数值全部为0
b = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
g = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
r = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)

# 复制图像通道里的数据
g[:, :] = img[:, :, 1]  # 复制 g 通道的数据


np.save("gchannel.npy",g)
g = np.load("gchannel.npy")

cv2.imshow("Green", g)
cv2.waitKey(0)
cv2.destroyAllWindows()

