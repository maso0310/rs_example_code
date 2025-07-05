import cv2 as cv
import numpy as np
# 載入圖片並轉換到HSV色彩空間
image = cv.imread('./01_Image/Lenna.png')
hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
# 定義藍紫色的HSV範圍
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([160, 255, 255])
# 創建遮罩，過濾出藍紫色區域
mask = cv.inRange(hsv_image, lower_blue, upper_blue)
# 將遮罩應用到原始圖片上，顯示結果
result = cv.bitwise_and(image, image, mask=mask)
cv.imshow('原圖', image)
cv.imshow('遮罩篩選後的圖片', result)
cv.waitKey()
cv.imwrite('./01_Image/Mask_Result.png', result)
