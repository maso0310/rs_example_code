import pandas as pd                     # 資料處理使用 Pandas 套件
from matplotlib import pyplot as plt    # 繪圖使用 matplotlib 套件

# ✅ 1. 讀取 Excel 檔案為 DataFrame（表格資料格式）
df = pd.read_excel('./02_Data/植生指標萃取結果範例.xlsx')

# ✅ 2. 輸出資料欄位名稱與原始資料形狀
columns_name = df.columns
print(f'資料欄位:\n{columns_name}')    # 印出欄位名稱供確認
print(f'原始資料形狀:\n{df.shape}')     # 印出資料總筆數與欄位數

# ✅ 3. 建立篩選條件：選取特定期別（例如110-1）與區域（例如A1）
df_filter = ((df['Period'] == '110-1') & (df['field'] == 'A1'))

# ✅ 4. 根據條件篩選資料
dt = df[df_filter]
print(f'目標資料形狀:\n{dt.shape}')      # 印出篩選後的資料筆數與欄位數

# ✅ 5. 萃取欄位為一維陣列（NumPy array）
DAT = dt['生育日數'].values       # X 軸：生育日數（Days after Transplant）
NDVI = dt['NDVI'].values         # Y 軸：NDVI 植生指標數值

# ✅ 6. 繪製折線圖（XY 散佈圖）
# X 軸為生育日數，Y 軸為 NDVI 數值
plt.plot(DAT, NDVI, '-o', color='blue', marker='o', linewidth=2, markersize=6)
plt.title(f'NDVI')                          # 圖片標題
plt.ylabel('NDVI values')                  # Y 軸標籤
plt.xlabel('Days after Transplant')        # X 軸標籤

# ✅ 7. 儲存圖片至指定路徑
plt.savefig('./03_Result/Figsure/NDVI_XY散佈圖.png')
print(f'圖片繪製完畢 路徑： ./03_Result/Figsure/NDVI_XY散佈圖.png')
