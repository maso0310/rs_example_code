import cv2 as cv
import os

# 圖片路徑
image_path = './01_Image/Lenna.png'

# 檢查圖片是否存在
if not os.path.exists(image_path):
    print("❌ 找不到圖片檔案，請確認路徑是否正確：", image_path)
    exit()

# 設定不同的讀取模式
modes = {
    "IMREAD_COLOR（彩色 BGR）": cv.IMREAD_COLOR,
    "IMREAD_GRAYSCALE（灰階）": cv.IMREAD_GRAYSCALE,
    "IMREAD_UNCHANGED（原始格式，含透明）": cv.IMREAD_UNCHANGED,
    "REDUCED_COLOR_2（1/2 彩色）": cv.IMREAD_REDUCED_COLOR_2,
    "REDUCED_COLOR_4（1/4 彩色）": cv.IMREAD_REDUCED_COLOR_4,
    "REDUCED_GRAYSCALE_2（1/2 灰階）": cv.IMREAD_REDUCED_GRAYSCALE_2,
}

# 逐一讀取與顯示圖片
for mode_name, mode_flag in modes.items():
    img = cv.imread(image_path, mode_flag)

    if img is None:
        print(f"❌ {mode_name} 模式讀取失敗")
        continue

    # 顯示圖片視窗
    cv.imshow(mode_name, img)

    # 輸出圖像資訊
    print(f"✅ {mode_name} 模式讀取成功")
    print("   shape：", img.shape)
    print("   dtype：", img.dtype)
    print("   通道數：", 1 if len(img.shape) == 2 else img.shape[2])
    print("-" * 50)

# 等待所有視窗，直到按下任意鍵關閉
cv.waitKey(0)
cv.destroyAllWindows()
