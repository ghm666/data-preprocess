import numpy as np
import cv2

# 定义旋转rotate函数
def rotate(image, angle, center=None, scale=1.0):
    # 获取图像尺寸
    (h, w) = image.shape[:2]

    # 若未指定旋转中心，则将图像中心设为旋转中心
    if center is None:
        center = (w / 2, h / 2)

    # 执行旋转
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))

    # 返回旋转后的图像
    return rotated

local_his = np.load("loacl_histom.npy")
cv2.imshow("clahe_demo", local_his)

flipped = cv2.flip(local_his, 1)
cv2.imshow("Flipped Horizontally", flipped)

rotated = rotate(local_his, 90)
cv2.imshow("Rotated by 90 Degrees", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()




