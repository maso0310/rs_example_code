import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA

# 載入鳶尾花資料集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 初始化 PCA，設定降維維度為2
pca = PCA(n_components=2)

# 對數據進行降維
X_pca = pca.fit_transform(X)

# 可視化降維後的數據
plt.figure(figsize=(8, 6))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', edgecolor='k', s=50)
plt.title('PCA of Iris Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(scatter, label='Species')
plt.show()
