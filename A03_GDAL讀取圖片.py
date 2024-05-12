from osgeo import gdal

# 打開 TIFF 文件
tif_input_path = './01_Image/UAV/tif/2022-10-10_BG_RGB_20m_Ortho.tif'
dataset = gdal.Open(tif_input_path)

# 讀取柵格數據
image = dataset.ReadAsArray()

# 獲取地理空間資訊
transform = dataset.GetGeoTransform()  # 獲得地理資訊變數
projection = dataset.GetProjection()   # 獲得投影資訊

# 投影變化參數包含:
# transform[0]：圖片左上角的x座標
# transform[1]：東西向的像素解析度
# transform[2]：旋轉角度，0代表圖像是北方朝上
# transform[3]：圖片左上角的y座標
# transform[4]：旋轉角度，0代表圖像是北方朝上
# transform[5]：南北向的像素解析度(通常為負值)

# 圖像的形狀訊息
width = dataset.RasterXSize    # 圖像寬度
height = dataset.RasterYSize   # 圖像高度
bands = dataset.RasterCount    # 圖像波段數

# 將資訊印出
print(f"圖片維度: {width} x {height}, 波段數量: {bands}")
print(f"空間資訊資料: {transform}")
print(f"投影座標系統: {projection}")

# 讀取並印出每個波段的統計訊息
for i in range(bands):
    band = dataset.GetRasterBand(i + 1)
    min, max, mean, std = band.ComputeStatistics(0) # 0是精準計算，1是允許使用近似方法
    print(f"波段 {i+1} - 最小值: {min}, 最大值: {max}, 平均: {mean}, 標準差: {std}")

# 关闭数据集
dataset = None
