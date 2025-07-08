from osgeo import gdal, ogr  # 匯入 GDAL 用於影像處理、OGR 用於向量圖層 (Shapefile) 操作
import os  # 匯入 OS 模組處理檔案與資料夾

# ✅ 1. 指定輸入檔案路徑
tif_file_path = './01_Image/UAV/tif/2022-10-10_BG_RGB_20m_Ortho.tif'  # 大型正射影像
shp_file_path = './01_Image/UAV/shapefile/example.shp'                # 用來切割的範圍 (Shapefile)

# ✅ 2. 開啟 Shapefile，取得圖層
shapefile = ogr.Open(shp_file_path)
layer = shapefile.GetLayer()

# ✅ 3. 逐一處理每一個圖層中的多邊形 Feature（多邊形區塊）
# enumerate(layer) 的意思是：對圖層中的每個要素 (feature) 同時取得「索引編號 i」和「要素本身 feature」
# 索引 i 會對應到每個 feature 在圖層中的 FID（Feature ID），可用於後續的條件篩選與命名
for i, feature in enumerate(layer):

    # ✅ 4. 建立輸出資料夾與影像檔案名稱
    output_path_dir = './03_Result'
    os.makedirs(output_path_dir, exist_ok=True)
    output_path = f'{output_path_dir}/clip_image_{i}.tif'

    # ✅ 5. 使用 gdal.Warp 根據每個多邊形 FID 來切割影像
    ds = gdal.Warp(
        output_path,
        tif_file_path,
        cutlineDSName=shp_file_path,
        cutlineWhere=f"FID = {i}",
        cropToCutline=True,
        dstNodata=255
    )

    # ✅ 顯示每個輸出檔案的路徑
    print(f'輸出： {output_path}')

# ✅ 6. 顯示完成訊息
print('✅ 所有圖塊切割完畢！')
