from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np
import os

# 圖片路徑
tif_input_path = './01_Image/UAV/tif/2022-10-10_BG_RGB_20m_Ortho.tif'

# ✅ 1. 開啟 GeoTIFF 影像
dataset = gdal.Open(tif_input_path)
if dataset is None:
    print("❌ 找不到檔案，請確認路徑是否正確。")
    exit()

# ✅ 2. 基本空間資訊
transform = dataset.GetGeoTransform()  # 地理轉換參數
projection = dataset.GetProjection()   # 投影資訊

# 📌 GeoTransform 含六個參數，依序為：
# transform[0]：圖片左上角像素對應的 X 座標（通常是西北角的實際經緯/投影座標）
# transform[1]：每個像素的 X 解析度（單位：公尺或度），即每個像素寬度
# transform[2]：旋轉參數（通常為 0），非 0 代表圖像有旋轉（例如航照偏移）
# transform[3]：圖片左上角像素對應的 Y 座標
# transform[4]：旋轉參數（通常為 0），非 0 表示有傾斜或旋轉
# transform[5]：每個像素的 Y 解析度（通常為負值，因為 Y 軸向下遞增）

# ✅ 3. 影像形狀資訊
width = dataset.RasterXSize
height = dataset.RasterYSize
bands = dataset.RasterCount

print(f"\n📐 影像尺寸：{width} x {height}")
print(f"📷 波段數量：{bands}")
print(f"🗺️ 空間參數：{transform}")
print(f"🧭 投影系統：\n{projection}")

# ✅ 4. 讀取所有波段為一個 numpy 陣列（shape: [band, height, width]）
image = dataset.ReadAsArray()

# ✅ 5. 顯示每個波段的統計資料與直方圖
for i in range(bands):
    band = dataset.GetRasterBand(i + 1)
    min_val, max_val, mean_val, std_val = band.ComputeStatistics(False)

    print(f"\n📊 波段 {i+1}:")
    print(f"   ▸ 最小值: {min_val}")
    print(f"   ▸ 最大值: {max_val}")
    print(f"   ▸ 平均值: {mean_val}")
    print(f"   ▸ 標準差: {std_val}")

    # 畫出波段的直方圖
    plt.figure()
    # 未將數值為255的像素排除
    plt.hist(image[i], bins=256, color='gray')
    # 將數值為255的像素排除
    # plt.hist(image[i][image[i]!=255], bins=256, color='gray')
    plt.title(f'Band {i+1} Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.grid(True)

plt.tight_layout()
plt.show()

# ✅ 6. 轉換圖像中心像素座標為地理座標（範例：中央像素）
center_x = width // 2
center_y = height // 2

geo_x = transform[0] + center_x * transform[1] + center_y * transform[2]
geo_y = transform[3] + center_x * transform[4] + center_y * transform[5]

print(f"\n📍 圖像中心像素位置：({center_x}, {center_y})")
print(f"   對應地理座標：({geo_x:.2f}, {geo_y:.2f})")

# ✅ 8. 關閉檔案
dataset = None
