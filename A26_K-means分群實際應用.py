# 匯入自定義的設定檔（df, X_variable_list 等）
from C01_設定檔 import *

# 匯入繪圖工具與模型套件
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# 擷取資料中的特徵欄位，轉成 numpy array 格式（樣本數 × 特徵數）
X = df[X_variable_list].values

# 使用 PCA 將高維特徵降維至 2 維，以便進行可視化與分群
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)  # shape = (樣本數, 2)

# 初始化 K-Means 分群模型
# n_clusters=9 表示希望將資料分為 9 群
# random_state=42 是為了保證結果的可重現性
kmeans = KMeans(n_clusters=9, random_state=42)

# 使用降維後的資料擬合 K-Means 模型，學習群集中心
kmeans.fit(X_pca)

# 預測每筆資料屬於哪一個群集，回傳每筆資料的分群標籤
labels = kmeans.predict(X_pca)  # shape = (樣本數,)

# 使用 Matplotlib 繪製散佈圖，觀察分群結果
# 資料點根據 K-Means 的分群結果 (labels) 上色
# cmap='viridis' 提供不同群集的顏色，edgecolor='k' 增加黑色邊框讓點更清楚
plt.scatter(
    X_pca[:, 0],    # X 軸為 PCA 第 1 主成分
    X_pca[:, 1],    # Y 軸為 PCA 第 2 主成分
    c=labels,       # 顏色依據群集標籤
    cmap='viridis',
    edgecolor='k'   # 黑色邊框
)

# 取得每個群集的中心位置（PCA 2 維空間中）
centers = kmeans.cluster_centers_

# 顯示群集中心：紅色半透明大圓點
plt.scatter(
    centers[:, 0],  # 中心點 X 座標
    centers[:, 1],  # 中心點 Y 座標
    c='red',        # 顏色紅色
    s=200,          # 點大小
    alpha=0.5       # 透明度
)

# 加上圖表標題與軸標籤
plt.title('K-means clustering on PCA-reduced rice panicle data')
plt.xlabel('Principal Component 1')  # X 軸名稱
plt.ylabel('Principal Component 2')  # Y 軸名稱

# 顯示圖表
plt.show()
