import glob                         # 用來讀取檔案路徑
from pathlib import Path            # 處理檔案與資料夾路徑
from osgeo import gdal              # 用來讀取與寫入 GeoTIFF 影像
import os                           # 建立資料夾用
from skimage.filters import threshold_otsu  # Otsu 閾值函式 (scikit-image)
import matplotlib.pyplot as plt
from tqdm import tqdm  # 顯示進度條

# ✅ 設定 matplotlib 字型為繁體中文支援字型
plt.rcParams['font.family'] = 'Microsoft JhengHei'  # 或 'DFKai-SB', 'MingLiU'

# ✅ 1. 取得所有結果資料夾中的 .tif 圖片路徑
image_path_list = glob.glob('./03_Result/*.tif')

# ✅ 2. 對每一張影像做處理
for i in tqdm(range(len(image_path_list)), desc='處理影像中'):
    image_path = image_path_list[i]                        # 單一影像的路徑
    image = gdal.Open(image_path).ReadAsArray() / 255.0    # 使用 gdal 讀取影像並正規化到 0~1
    image_name = Path(image_path).stem                     # 取得影像檔案名稱（不含副檔名）

    # ✅ 3. 分別取出 R、G、B 三個通道
    R = image[0, :, :]  # 紅色通道
    G = image[1, :, :]  # 綠色通道
    B = image[2, :, :]  # 藍色通道

    # ✅ 4. 計算 ExG (Excess Green Index)：強化綠色植物特徵
    ExG = 2 * G - R - B

    # ✅ 5. 過濾掉 ExG == 0 的像素再執行 Otsu
    ExG_nonzero = ExG[ExG > 0]  # 去除背景或空白區域
    threshold_val = threshold_otsu(ExG_nonzero)
    mask = (ExG > threshold_val) * 1.0  # 超過閾值的位置為 1，其他為 0，產生遮罩

    # ✅ 6. 使用遮罩將原始影像乘上，將非植生區設為黑色
    new_image = image * mask * 255.0   # 回復為 0–255 數值區間（浮點數）

    # ✅ 7. 建立輸出資料夾（若尚未存在）
    os.makedirs('./03_Result/Otsu', exist_ok=True)

    # ✅ 8. 可視化 Otsu 閾值在 ExG 分布中的位置
    plt.figure(figsize=(6, 4))
    plt.hist(ExG_nonzero.ravel(), bins=50, color='green', alpha=0.7)
    plt.axvline(threshold_val, color='red', linestyle='--', label=f'Otsu 閾值 = {threshold_val:.4f}')
    plt.title(f'{image_name} - ExG 分布與 Otsu 閾值')
    plt.xlabel('ExG 值')
    plt.ylabel('像素數量')
    plt.ticklabel_format(axis='y', style='plain')  # 這也可加強強制為一般數字
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'./03_Result/Otsu/Otsu_threshold_ExG_{i}.jpg', dpi=300)

    # ✅ 9. 將結果寫出成新的 GeoTIFF 檔案
    output_path = f'./03_Result/Otsu/Otsu_Result_{i}.tif'
    image_writer = gdal.Translate(f'./03_Result/Otsu/Otsu_Result_{i}.tif',   image_path, outputType=gdal.GDT_Byte)
    image_writer.WriteArray(new_image)

print('✅ 所有影像已完成 Otsu 二值遮罩處理！')
