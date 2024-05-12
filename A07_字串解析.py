import glob
from pathlib import Path 

# 獲得目標路徑
tif_image_path = glob.glob('./*/*/*/*.tif')[0]

# 檔案名稱
file_name = Path(tif_image_path).stem
print(f'檔案名稱: {file_name}')

# 透過字串解析，由檔案名稱中取得檔案拍攝的日期
date = file_name.split('_')[0].replace('-', '')
print(f'拍攝日期: {date}')
