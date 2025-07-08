import glob
from pathlib import Path

# ✅ 1. 使用 glob 搜尋所有子目錄下的 .tif 檔案
tif_files = glob.glob('./**/*.tif', recursive=True)

# ✅ 2. 檢查是否有找到任何影像檔
if not tif_files:
    print("❌ 沒有找到任何 .tif 影像檔案，請確認資料夾或副檔名是否正確。")
else:
    # ✅ 3. 取第一個找到的 .tif 檔案作為範例
    tif_image_path = tif_files[0]

    # ✅ 4. 使用 pathlib.Path 物件處理路徑
    # 上層資料夾
    parent_dir = Path(tif_image_path).parent

    # 不含副檔名的檔名
    file_name = Path(tif_image_path).stem

    # 副檔名（例如 .tif）
    file_ext = Path(tif_image_path).suffix

    # ✅ 5. 印出結果
    print("📄 影像路徑資訊：\n")
    print(f"🧭 目標完整路徑: {tif_image_path}")
    print(f"📁 上層資料夾  : {parent_dir}")
    print(f"📌 圖片檔名    : {file_name}")
    print(f"📎 副檔名      : {file_ext}")
