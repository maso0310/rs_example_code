import cv2 as cv               # 匯入 OpenCV 套件，處理影像用
import numpy as np            # 匯入 NumPy，用於處理陣列與數值運算

# ✅ 1. 讀取原始圖片，並轉換為 HSV 色彩空間
image = cv.imread('./01_Image/Lenna.png')           # 使用 OpenCV 讀取圖片（BGR 格式）
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)          # 將 BGR 轉為 HSV，適合做顏色範圍篩選

# ✅ 2. 建立一個可調整大小的視窗來顯示結果
cv.namedWindow('Result', cv.WINDOW_NORMAL)          # 建立視窗並允許使用者縮放

# ✅ 3. 建立 HSV 各通道的上下界滑桿（Hue: 0-179, Saturation/Value: 0-255）
# lambda x: None 是滑桿需要的回呼函式（callback），這裡用空函式避免出錯
cv.createTrackbar('H Lower', 'Result', 100, 179, lambda x: None)  # 色相下限
cv.createTrackbar('H Upper', 'Result', 160, 179, lambda x: None)  # 色相上限
cv.createTrackbar('S Lower', 'Result', 50, 255, lambda x: None)   # 飽和度下限
cv.createTrackbar('S Upper', 'Result', 255, 255, lambda x: None)  # 飽和度上限
cv.createTrackbar('V Lower', 'Result', 50, 255, lambda x: None)   # 明亮度下限
cv.createTrackbar('V Upper', 'Result', 255, 255, lambda x: None)  # 明亮度上限

# ✅ 4. 進入即時篩選迴圈
while True:
    # 讀取滑桿當前數值
    h_lower = cv.getTrackbarPos('H Lower', 'Result')
    h_upper = cv.getTrackbarPos('H Upper', 'Result')
    s_lower = cv.getTrackbarPos('S Lower', 'Result')
    s_upper = cv.getTrackbarPos('S Upper', 'Result')
    v_lower = cv.getTrackbarPos('V Lower', 'Result')
    v_upper = cv.getTrackbarPos('V Upper', 'Result')

    # 組成 HSV 的上下界 NumPy 陣列
    lower_bound = np.array([h_lower, s_lower, v_lower])  # 最低 HSV
    upper_bound = np.array([h_upper, s_upper, v_upper])  # 最高 HSV

    # 建立遮罩，符合條件的位置變成白（255），其餘為黑（0）
    mask = cv.inRange(hsv, lower_bound, upper_bound)

    # 將遮罩套用到原始影像，僅保留選中的顏色範圍
    result = cv.bitwise_and(image, image, mask=mask)

    # 顯示結果
    cv.imshow('Result', result)

    # 如果使用者按下 'q'，跳出迴圈並關閉程式
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# ✅ 5. 關閉所有 OpenCV 視窗
cv.destroyAllWindows()
