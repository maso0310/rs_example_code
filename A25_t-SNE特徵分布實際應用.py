from C01_設定檔 import *
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
import numpy as np

# 抓取特徵數值
X = df[X_variable_list].values

# 將期作標籤抓出
periods = df['Period'].values

# 設定t-SNE模型，n為降維的維度
tsne = TSNE(n_components=2, random_state=42)

# 對指定數據進行降維處理
X_tsne = tsne.fit_transform(X)

# 繪製散佈圖
# 創建一個顏色字典，每個唯一個期作別對應一個顏色
unique_periods = np.unique(periods)
colors = plt.cm.jet(np.linspace(0, 1, len(unique_periods)))
color_map = {period: color for period, color in zip(unique_periods, colors)}

# 繪圖
for period in unique_periods:
    indices = periods == period
    plt.scatter(X_tsne[indices, 0], X_tsne[indices, 1], c=[color_map[period]], label=period, s=3, alpha=0.7)

plt.xlabel('t-SNE Feature 1')
plt.ylabel('t-SNE Feature 2')
plt.title('t-SNE Visualization of Data Colored by Period')
plt.legend(title='Period')
plt.show()
