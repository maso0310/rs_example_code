import glob
from pathlib import Path
# 獲得目標路徑
tif_image_path = glob.glob('./*/*/*/*.tif')[0]
# 上層資料夾
parent_dir = Path(tif_image_path).parent
# 檔案名稱
file_name = Path(tif_image_path).stem
# 檔案副檔名
file_ext = Path(tif_image_path).suffix
print(f'目標路徑: {tif_image_path}')
print(f'上層資料夾: {parent_dir}')
print(f'圖片檔案名稱: {file_name}')
print(f'檔案副檔名: {file_ext}')
