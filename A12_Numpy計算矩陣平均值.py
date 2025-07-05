import cv2 as cv
import numpy as np
# 讀取結果圖並轉換到HSV色彩空間
image = cv.imread('./01_Image/Mask_Result.png')
hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
# 創建非黑色像素掩碼並計算非黑色像素的HSV平均值
mask = np.any(hsv_image != [0, 0, 0], axis=2)
average_hsv = np.mean(hsv_image[mask], axis=0)
# 輸出平均值
print(f"cleaH 的平均值: {average_hsv[0]:.2f}")
print(f"S 的平均值: {average_hsv[1]:.2f}")
print(f"V 的平均值: {average_hsv[2]:.2f}")
