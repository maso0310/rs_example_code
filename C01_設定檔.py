# 匯入 pandas 套件，用於資料處理（如讀取 CSV、操作表格）
import pandas as pd

# -------------------------------
# 資料讀取與清理
# -------------------------------

# 讀取稻穗顏色與含水率調查資料的 CSV 檔案
# 設定 low_memory=False 可以避免 Pandas 因資料型別混合而分段處理欄位造成的警告
df = pd.read_csv('./02_Data/稻穗榖粒含水量調查資料與顏色特徵.csv', low_memory=False)

# 篩選資料：只保留 HMC（穀粒含水率）不為 'Unknow' 的資料列
# 這是為了確保目標變數是可用的數值格式
df = df[(df['HMC'] != 'Unknow')]

# -------------------------------
# 欄位定義
# -------------------------------

# 特徵數值欄位清單（X），包含多種顏色空間與影像統計特徵
X_variable_list = [
    # 原始 RGB 色彩空間
    'R','G','B',

    # HSV 色彩空間（H1 表色相、S1 飽和度、V1 明度）
    'H1','S1','V1',

    # HSL 或 Lab 色彩空間轉換
    'L2','S2','L','a','b',

    # YCbCr 色彩空間
    'Y','Cr','Cb',

    # 植生指標與比值型特徵
    'NDI','GI','RGRI',

    # 對比校正後的特徵
    'RC','GC','BC',
    'H1C','S1C','V1C',
    'L2C','S2C','LC',
    'aC','bC','YC','CrC','CbC',
    'NDIC','GIC','RGRIC',

    # 校正色卡顏色數值統計
    'B_RGB_avg', 'G_RGB_avg', 'W_RGB_avg',      # 黑、灰、白 RGB 平均值
    'B_RGB_R', 'B_RGB_G', 'B_RGB_B',            # 黑區 RGB
    'G_RGB_R', 'G_RGB_G', 'G_RGB_B',            # 灰區 RGB
    'W_RGB_R', 'W_RGB_G', 'W_RGB_B'             # 白區 RGB
]

# 標記欄位清單（Y），只包含目標變數：HMC（穀粒含水率）
Y_variable_list = ['HMC']
