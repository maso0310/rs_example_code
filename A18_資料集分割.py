import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('./02_Data/稻穗榖粒含水量調查資料與顏色特徵.csv')

train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

print('訓練資料集形狀', train_df.shape)
print('測試資料集形狀', test_df.shape)
