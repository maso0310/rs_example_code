import glob

# 輸出第一層的所有資料夾與檔案的路徑
# print(glob.glob('./*'))

# 搜尋第四層目錄下的所有 .tif 檔案（僅一層）
print(glob.glob('./*/*/*/*.tif'))

# 搜尋所有子目錄下的 .tif 檔案（不限層級）
glob.glob('./**/*.tif', recursive=True)



'''
📌 什麼是 glob？
glob 模組是 Python 中用來依據通配符模式（wildcard）來搜尋檔案與資料夾的工具，簡單快速，非常適合用來處理檔案批次讀取與管理。

🔍 常見通配符語法說明：
通配符	說明
*	任意字元（不含資料夾分隔符）
**	任意層級的目錄（需搭配 recursive=True）

🧰 常見實務應用補充：
功能	範例說明
取得特定副檔名	*.tif, *.jpg, *.csv
過濾特定檔案命名	*NDVI*.tif, *2023*.tif
遞迴所有子資料夾	使用 **/*.tif 並搭配 recursive=True
'''