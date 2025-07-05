import glob 
from pathlib import Path
from osgeo import gdal
import numpy as np
import os
import csv

# 建立資料夾
os.makedirs('./03_Result/CSV', exist_ok=True)
# 建立CSV檔案
with open('./03_Result/CSV/Result.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['image_name', 'ExG', 'NDI', 'GI', 'RGRI'])

    # 由指定圖片路徑列表建立迴圈
    for image_path in glob.glob('./03_Result/Otsu/*.tif'):
        # 讀取圖片與名稱
        image = gdal.Open(image_path).ReadAsArray() / 255.0
        image_name = Path(image_path).stem

        # 將每個波段分離
        R = image[0,:,:]
        G = image[1,:,:]
        B = image[2,:,:]

        # 建立一個遮罩，忽略掉全黑像素
        valid_mask = (R > 0) & (G > 0) & (B > 0)

        # 計算有效像素的植生指標
        ExG = np.where(valid_mask, (2 * G) - R - B, np.nan)
        NDI = np.where(valid_mask, (G - R) / (G + R + 1e-10), np.nan)
        GI = np.where(valid_mask, G / (R + 1e-10), np.nan)
        RGRI = np.where(valid_mask, R / (G + 1e-10), np.nan)

        # 計算植生指標，並且忽略空值
        ExG_mean = np.nanmean(ExG)
        NDI_mean = np.nanmean(NDI)
        GI_mean = np.nanmean(GI)
        RGRI_mean = np.nanmean(RGRI)

        # 將結果寫入CSV檔案中
        writer.writerow([image_name, ExG_mean, NDI_mean, GI_mean, RGRI_mean])
print(f'資料寫入完畢 檔案位置： ./03_Result/CSV/Result.csv')