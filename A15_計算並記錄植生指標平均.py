import glob                        # 用來讀取符合條件的檔案清單
from pathlib import Path           # 處理檔名與路徑
from osgeo import gdal             # GDAL 用來讀取 GeoTIFF 影像資料
import numpy as np                # 數值計算用的套件
import os                         # 用來建立資料夾
import csv                        # 寫入 CSV 檔案用

# ✅ 建立輸出資料夾（若尚未存在）
os.makedirs('./03_Result/CSV', exist_ok=True)

# ✅ 建立 CSV 檔案並寫入表頭
with open('./03_Result/CSV/Result.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['image_name', 'ExG', 'NDI', 'GI', 'RGRI'])  # 表頭欄位名稱

    # ✅ 讀取所有 Otsu 處理過的 GeoTIFF 影像檔
    for image_path in glob.glob('./03_Result/Otsu/*.tif'):
        # ✅ 使用 GDAL 讀取影像並正規化為 0~1（避免後續除以 255）
        image = gdal.Open(image_path).ReadAsArray() / 255.0
        image_name = Path(image_path).stem  # 取得影像檔名（不含副檔名）

        # ✅ 將三個波段分別對應到 R、G、B
        R = image[0, :, :]
        G = image[1, :, :]
        B = image[2, :, :]

        # ✅ 建立遮罩，排除全黑像素（背景區域）
        valid_mask = (R > 0) & (G > 0) & (B > 0)

        # ✅ 計算 4 種植生指標（排除背景，否則設為 NaN）
        ExG = np.where(valid_mask, (2 * G) - R - B, np.nan)                     # Excess Green
        NDI = np.where(valid_mask, (G - R) / (G + R + 1e-10), np.nan)          # Normalized Difference Index
        GI = np.where(valid_mask, G / (R + 1e-10), np.nan)                     # Green Index
        RGRI = np.where(valid_mask, R / (G + 1e-10), np.nan)                   # Red-Green Ratio Index

        # ✅ 分別計算每個指標的有效像素平均值（忽略 NaN）
        ExG_mean = np.nanmean(ExG)
        NDI_mean = np.nanmean(NDI)
        GI_mean = np.nanmean(GI)
        RGRI_mean = np.nanmean(RGRI)

        # ✅ 將平均值結果寫入 CSV 檔案
        writer.writerow([image_name, ExG_mean, NDI_mean, GI_mean, RGRI_mean])

# ✅ 輸出完成訊息
print(f'資料寫入完畢 檔案位置： ./03_Result/CSV/Result.csv')
