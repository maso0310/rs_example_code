from C01_設定檔 import *
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# 抓取特徵數值
X = df[X_variable_list].values

# 使用PCA降維至2維
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# 初始化Kmeans模型，設定分群為9類
kmeans = KMeans(n_clusters=9, random_state=42)

# 擬合Kmeans模型
kmeans.fit(X_pca)

# 預測聚類標籤
labels = kmeans.predict(X_pca)

# 可視化聚類結果
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', edgecolor='k')
centers = kmeans.cluster_centers_

# 將聚類中心以紅色標註
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5)  
plt.title('K-means clustering on PCA-reduced rice panicle data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
