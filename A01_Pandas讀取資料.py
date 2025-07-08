import pandas as pd
import matplotlib.pyplot as plt

# 📌 1. 讀取 Excel 檔案
df = pd.read_excel('./02_Data/植生指標萃取結果範例.xlsx')

# 📌 2. 顯示資料基本資訊
print("欄位名稱：", df.columns.tolist())
print("\n資料概況：")
print(df.info())
print("\n數值欄位統計：")
print(df.describe())

# 📌 3. 檢查是否有缺值
print("\n每欄缺值數量：")
print(df.isnull().sum())

# 📌 4. 篩選 N_type 為 'N3' 且 W_type 為 'CP' 的資料列
dt_filter = (df['N_type'] == 'N3') & (df['W_type'] == 'CP')
dt = df[dt_filter]
print("\n篩選後的資料（N_type='N3' 且 W_type='CP'）：")
print(dt)

# 📌 5. 對 NDVI 欄位進行基本統計與視覺化
if 'NDVI' in df.columns:
    print("\nNDVI 各類 N_type 平均值：")
    print(df.groupby('N_type')['NDVI'].mean())

    # 繪製盒狀圖（Boxplot）比較各 N_type 的 NDVI 分布
    df.boxplot(column='NDVI', by='N_type')
    plt.title('各類 N_type 的 NDVI 盒狀圖')
    plt.suptitle('')
    plt.xlabel('N_type')
    plt.ylabel('NDVI')
    plt.tight_layout()
    plt.show()

    # 📌 6. 新增 NDVI 標準化欄位（Z-score）
    df['NDVI_zscore'] = (df['NDVI'] - df['NDVI'].mean()) / df['NDVI'].std()
    print("\nNDVI 標準化後前 5 筆：")
    print(df[['NDVI', 'NDVI_zscore']].head())

# 📌 7. 匯出篩選後的結果為新的 Excel 檔案
output_path = './02_Data/N3_CP篩選結果.xlsx'
dt.to_excel(output_path, index=False)
print(f"\n✅ 篩選結果已匯出至：{output_path}")
