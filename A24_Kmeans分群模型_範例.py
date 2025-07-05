import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

# 載入鳶尾花資料集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 初始化 K-means，設置分群數量為 3 (因為鳶尾花分類有三種)
kmeans = KMeans(n_clusters=3, random_state=42)

# 擬合模型
kmeans.fit(X)

# 預測聚類標籤
labels = kmeans.predict(X)

# 可視化聚類結果 可视化聚类结果
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', edgecolor='k')
centers = kmeans.cluster_centers_

# 將聚類中心以紅色標註
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5)  
plt.title('K-means clustering on Iris dataset')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.show()
