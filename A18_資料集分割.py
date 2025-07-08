# 載入 pandas 與 scikit-learn 的 train_test_split 函數
import pandas as pd
from sklearn.model_selection import train_test_split

# 讀取 CSV 檔案，這裡的檔案包含稻穗的含水量調查與顏色特徵資料
df = pd.read_csv('./02_Data/稻穗榖粒含水量調查資料與顏色特徵.csv')

# 使用 train_test_split 將資料集拆分為訓練集與測試集
# test_size=0.2 表示將 20% 的資料分配為測試資料，其餘 80% 為訓練資料
# random_state=42 為亂數種子，確保每次執行結果一致（可重現性）
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# 顯示分割後資料集的形狀（資料筆數與欄位數）
print('訓練資料集形狀:', train_df.shape)
print('測試資料集形狀:', test_df.shape)

# 可選：查看資料前幾列做確認
print('\n訓練資料集範例:')
print(train_df.head())

print('\n測試資料集範例:')
print(test_df.head())
