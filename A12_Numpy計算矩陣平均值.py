import cv2 as cv            # 匯入 OpenCV，用來處理圖像
import numpy as np         # 匯入 NumPy，進行矩陣與數值運算

# ✅ 1. 讀取遮罩處理後的圖片（僅保留特定顏色範圍）
image = cv.imread('./01_Image/Mask_Result.png')  # 圖片為遮罩過後的圖，背景為黑色，主體為保留顏色區域

# ✅ 2. 將 BGR 影像轉換成 HSV 色彩空間
hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)  # HSV 更適合分析色相與光影資訊

# ✅ 3. 建立遮罩：篩選出所有「非黑色」像素位置
# 只要該像素的 HSV 不等於 [0, 0, 0]，就視為保留區域（背景通常為黑色）
mask = np.any(hsv_image != [0, 0, 0], axis=2)  # axis=2 表示在每個像素的三個通道比較

# ✅ 4. 計算非黑色區域（即主體部分）的 HSV 三通道平均值
# 將三通道在遮罩位置的值取出後，逐通道計算平均
average_hsv = np.mean(hsv_image[mask], axis=0)

# ✅ 5. 輸出主體區域的平均 HSV 值（色相、飽和度、明亮度）
print(f"H（色相）平均值: {average_hsv[0]:.2f}")
print(f"S（飽和度）平均值: {average_hsv[1]:.2f}")
print(f"V（明亮度）平均值: {average_hsv[2]:.2f}")
