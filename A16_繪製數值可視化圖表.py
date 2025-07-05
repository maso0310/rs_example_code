import pandas as pd
from matplotlib import pyplot as plt
# 讀取excel檔案為dataframe
df = pd.read_excel('./02_Data/植生指標萃取結果範例.xlsx')

# 輸出欄位名稱
columns_name = df.columns
print(f'資料欄位:\n{columns_name}')
print(f'原始資料形狀:\n{df.shape}')

# 設定資料篩選器
df_filter = ((df['Period']=='110-1') & (df['field']=='A1'))
dt = df[df_filter]
print(f'目標資料形狀:\n{dt.shape}')

# 萃取特定的數列
DAT = dt['生育日數'].values
NDVI = dt['NDVI'].values

# 建立xy分布圖
# X軸為插秧後的生育日數，Y軸為NDVI數值
# color、marker可調整標記顏色與樣式
plt.plot(DAT, NDVI, '-o', color='blue', marker='o', linewidth=2, markersize=6)
plt.title(f'NDVI')
plt.ylabel('NDVI values')
plt.xlabel('Days after Transplant')
plt.savefig('./03_Result/Figsure/NDVI_XY散佈圖.png')
print(f'圖片繪製完畢 路徑： ./03_Result/Figsure/NDVI_XY散佈圖.png')