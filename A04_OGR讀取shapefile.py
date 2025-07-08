from osgeo import ogr

# ✅ 1. 設定 Shapefile 檔案路徑
shp_input_path = './01_Image/UAV/shapefile/example.shp'

# ✅ 2. 指定使用 ESRI Shapefile 格式的驅動器
driver = ogr.GetDriverByName('ESRI Shapefile')

# ✅ 3. 開啟 Shapefile 資料（0 = 只讀模式，1 = 可寫入模式）
dataSource = driver.Open(shp_input_path, 0)

# ✅ 4. 檢查檔案是否成功開啟
if dataSource is None:
    print("❌ 無法開啟 Shapefile，請檢查路徑是否正確。")
else:
    # ✅ 5. 取得圖層（layer），通常每個 shapefile 只有一層
    layer = dataSource.GetLayer()

    # ✅ 6. 計算圖層中有多少個 feature（例如多邊形、點、線）
    featureCount = layer.GetFeatureCount()
    print(f"📦 Shapefile 的特徵筆數（features）: {featureCount}")

    # ✅ 7. 逐一瀏覽每筆 feature（如每個地塊、線段、測站等）
    for feature in layer:
        print("🆔 特徵 ID (FID):", feature.GetFID())  # 特徵的唯一 ID

        # ✅ 取得幾何物件（例如 Point, Polygon）
        geom = feature.GetGeometryRef()
        print("📐 幾何類型:", geom.GetGeometryName())  # 例如 POLYGON、POINT、LINESTRING

        # ✅ 印出屬性欄位（Attribute Table）
        print("📋 屬性值：")
        for i in range(feature.GetFieldCount()):
            field_name = feature.GetFieldDefnRef(i).GetName()
            field_value = feature.GetField(i)
            print(f"   {field_name}: {field_value}")
        print("-" * 30)

    # ✅ 8. 關閉資料來源
    dataSource = None


'''
❓常見問題補充：
Q1:如何取得欄位名稱？	
A1:使用 feature.GetFieldDefnRef(i).GetName()

Q2:Shapefile 有多圖層嗎？	沒有，每個 Shapefile 通常只包含一個 Layer
A2:幾何類型有哪些？	POINT、LINESTRING、POLYGON、MULTIPOLYGON 等
'''