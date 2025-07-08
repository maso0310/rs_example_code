# 匯入事先設定好的變數（df, X_variable_list 等）來自自訂模組 C01_設定檔
from C01_設定檔 import *

# 匯入 t-SNE 模型與繪圖工具
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
import numpy as np

# 從資料集中取出特徵數值（X 變數），並轉成 numpy 格式
X = df[X_variable_list].values  # shape = (樣本數, 特徵數)

# 從資料集中取出期作別欄位（例如 110-1、110-2、111-1 等）
periods = df['Period'].values   # shape = (樣本數,)

# 建立 t-SNE 模型：將高維資料降到 2 維，便於視覺化
tsne = TSNE(n_components=2, random_state=42)  # random_state 確保結果一致

# 執行降維處理，產生新的 2 維資料點位置
X_tsne = tsne.fit_transform(X)  # shape = (樣本數, 2)

# 取得所有唯一的期作別，並為每個期作分配一種顏色
unique_periods = np.unique(periods)  # e.g. ['110-1', '110-2', '111-1']
colors = plt.cm.jet(np.linspace(0, 1, len(unique_periods)))  # 在 jet 色階上等距產生顏色
color_map = {period: color for period, color in zip(unique_periods, colors)}  # 建立顏色對應表

# 根據每個期作別，分別畫出其對應資料點
for period in unique_periods:
    # 找出屬於當前期作的資料索引
    indices = periods == period
    
    # 畫出該期作別的資料點，顏色對應 color_map，點大小設為 3，透明度 0.7
    plt.scatter(
        X_tsne[indices, 0],      # X 軸（第 1 主特徵）
        X_tsne[indices, 1],      # Y 軸（第 2 主特徵）
        c=[color_map[period]],   # 使用對應期作的顏色
        label=period,            # 圖例標籤
        s=3,                     # 點大小
        alpha=0.7                # 點透明度
    )

# 加上圖表標籤與標題
plt.xlabel('t-SNE Feature 1')                       # X 軸名稱
plt.ylabel('t-SNE Feature 2')                       # Y 軸名稱
plt.title('t-SNE Visualization of Data Colored by Period')  # 圖表標題

# 顯示圖例，標題為 'Period'
plt.legend(title='Period')

# 顯示圖表
plt.show()
