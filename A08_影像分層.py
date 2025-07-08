import cv2 as cv
import glob
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# ✅ 設定 matplotlib 字型為繁體中文支援字型
plt.rcParams['font.family'] = 'Microsoft JhengHei'  # 或 'DFKai-SB', 'MingLiU'

# ✅ 1. 使用 glob 找到圖片檔案
image_path = glob.glob('./01_Image/Lenna.png')[0]
image_name = Path(image_path).stem

# ✅ 2. 使用 OpenCV 讀取圖片（BGR 彩色格式）
image = cv.imread(image_path)

# ✅ 3. 分離 BGR 三個通道
B = image[:, :, 0]
G = image[:, :, 1]
R = image[:, :, 2]

# ✅ 4. 顯示各通道（灰階）
cv.imshow(f'{image_name} - 藍色通道', B)
cv.imshow(f'{image_name} - 綠色通道', G)
cv.imshow(f'{image_name} - 紅色通道', R)

# ✅ 5. 繪製三色直方圖
plt.figure(figsize=(10, 5))
plt.title(f"{image_name} 各通道像素分布直方圖")
plt.xlabel("像素值（0~255）")
plt.ylabel("像素數量（Pixel Count）")

plt.hist(B.ravel(), bins=256, color='blue', alpha=0.5, label='藍色 Blue')
plt.hist(G.ravel(), bins=256, color='green', alpha=0.5, label='綠色 Green')
plt.hist(R.ravel(), bins=256, color='red', alpha=0.5, label='紅色 Red')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ✅ 6. 等待關閉
cv.waitKey(0)
cv.destroyAllWindows()
