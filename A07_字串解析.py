import glob
from pathlib import Path

# ✅ 1. 使用 glob 遞迴搜尋所有 .tif 影像檔案
tif_files = glob.glob('./**/*.tif', recursive=True)

# ✅ 2. 確認至少有一筆影像檔案
if not tif_files:
    print("❌ 沒有找到任何 .tif 檔案，請確認路徑與副檔名")
else:
    # ✅ 3. 取第一筆影像檔案作為範例
    tif_image_path = tif_files[0]

    # ✅ 4. 使用 pathlib 提取檔案名稱（不含副檔名）
    file_name = Path(tif_image_path).stem
    print(f"📄 檔案名稱: {file_name}")

    # ✅ 5. 解析檔名中的日期（假設格式為 yyyy-mm-dd_內容.tif）
    # 先用 _ 拆分，再取第 0 段，移除 -
    date = file_name.split('_')[0].replace('-', '')
    print(f"📅 拍攝日期: {date}")
