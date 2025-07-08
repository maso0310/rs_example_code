import os
import glob
from osgeo import gdal

# 初始化計數器 i，用於輸出檔案命名
i = 0

# 取得所有 ./03_Result 資料夾下的 .tif 影像路徑
for image_path in glob.glob('./03_Result/*.tif'):
    # 使用 GDAL 開啟影像並讀取為 numpy 陣列 (shape: [bands, height, width])
    image = gdal.Open(image_path).ReadAsArray() / 255.0  # 將像素值標準化到 0~1

    # 將影像分離為 R、G、B 三個波段
    R = image[0, :, :]
    G = image[1, :, :]
    B = image[2, :, :]

    # 計算 ExG (Excess Green) 指標：ExG = 2G - R - B
    ExG = (2 * G) - R - B

    # 建立輸出資料夾（若尚未存在）
    os.makedirs('./03_Result/VIs', exist_ok=True)
    image_writer = gdal.Translate(f'./03_Result/VIs/ExG_{i}.tif', image_path, bandList=[1], outputType=gdal.GDT_Float32)
    image_writer.WriteArray(ExG)
    i+=1
    print(f'輸出： ./03_Result/VIs/ExG_{i}.tif')

print('植生指標計算與繪圖完畢！')
