import cv2 as cv
import glob
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

# ✅ 設定 matplotlib 字型為繁體中文支援字型
plt.rcParams['font.family'] = 'Microsoft JhengHei'  # 或 'DFKai-SB', 'MingLiU'

# ✅ 1. 搜尋圖片
image_list = glob.glob('./*/*.png')
if not image_list:
    raise FileNotFoundError("❌ 找不到任何 PNG 圖片，請確認路徑是否正確！")

image_path = image_list[0]  # 取第一張圖
image = cv.imread(image_path)
gray = image[:,:,2]

# ✅ 2. 固定閾值與 Otsu 二值化
ret_fixed, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
ret_otsu, otsu = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# ✅ 顯示圖片結果（選擇性開啟）
cv.imshow('藍光波段圖', gray)
cv.imshow('基礎二值化', binary)
cv.imshow('Otsu 二值化', otsu)

# ✅ 3. 顯示直方圖
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# 🎯 固定閾值直方圖
axs[0].hist(gray.ravel(), bins=256, range=(0, 256), color='gray')
axs[0].axvline(x=127, color='red', linestyle='--', label='固定閾值 = 127')
axs[0].set_title('灰階圖像直方圖（固定閾值）')
axs[0].set_xlabel('像素值 (0~255)')
axs[0].set_ylabel('像素數量')
axs[0].legend()
axs[0].grid(True)

# 🎯 Otsu 自動分割直方圖
axs[1].hist(gray.ravel(), bins=256, range=(0, 256), color='gray')
axs[1].axvline(x=ret_otsu, color='red', linestyle='--', label=f'Otsu 閾值 = {ret_otsu:.2f}')
axs[1].set_title('灰階圖像直方圖（Otsu 二值化）')
axs[1].set_xlabel('像素值 (0~255)')
axs[1].set_ylabel('像素數量')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()

print(f"Otsu 自動計算出的最佳閾值為: {ret_otsu:.2f}")
cv.waitKey(0)
cv.destroyAllWindows()
