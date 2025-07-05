from osgeo import gdal, ogr
import os

# 指定TIF和Shapefile的路徑
tif_file_path = './01_Image/UAV/tif/2022-10-10_BG_RGB_20m_Ortho.tif'
shp_file_path = './01_Image/UAV/shapefile/example.shp'

# 打開Shapefile
shapefile = ogr.Open(shp_file_path)
layer = shapefile.GetLayer()

# 為每個特徵創建切割後的小塊TIF
for i, feature in enumerate(layer):

    # 創建目標TIF文件的路徑
    output_path_dir = './03_Result'
    os.makedirs(output_path_dir, exist_ok=True)
    output_path = f'{output_path_dir}/clip_image_{i}.tif'

    # 使用gdal.Warp切割
    ds = gdal.Warp(output_path,                     # 輸出路徑
                   tif_file_path,                   # 輸入tif檔案
                   cutlineDSName=shp_file_path,     # 輸入shp檔案
                   cutlineWhere=f"FID = {i}",       # 指定的FID
                   cropToCutline=True,              # 指定tif座標與shp相同
                   dstNodata=255)                   # No Data定義為255

print('切割完畢！')