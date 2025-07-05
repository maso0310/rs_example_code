from osgeo import ogr

# 打開 Shapefile
shp_input_path = './01_Image/UAV/shapefile/example.shp'
driver = ogr.GetDriverByName('ESRI Shapefile')
dataSource = driver.Open(shp_input_path, 0)  # 0 means read-only. 1 means writeable.

# 檢查 shapefile 是否成功開啟
if dataSource is None:
    print("沒辦法打開檔案")
else:
    layer = dataSource.GetLayer()
    featureCount = layer.GetFeatureCount()
    print(f"Shapefile的特徵資料筆數: {featureCount}")

    # 遍历每个 feature，打印属性表信息
    for feature in layer:
        print("特徵 ID: ", feature.GetFID())
        geom = feature.GetGeometryRef()
        print("shapefile類別: ", geom.GetGeometryName())
        
    # 关闭数据源
    dataSource = None