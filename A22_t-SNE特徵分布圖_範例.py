import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.manifold import TSNE
import numpy as np

# 載入鳶尾花資料集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 設定t-SNE模型，n為降維的維度
tsne = TSNE(n_components=2, random_state=42)

# 對指定數據進行降維處理
X_tsne = tsne.fit_transform(X)

# 建立顏色列表
colors = ['red', 'green', 'blue']

# 可視化降維後的數據
for idx, cl in enumerate(np.unique(y)):
    plt.plot()
    plt.scatter(X_tsne[y == cl, 0], X_tsne[y == cl, 1], c=colors[idx], label=iris.target_names[cl])

# 繪製圖表
plt.xlabel('t-SNE feature 1')
plt.ylabel('t-SNE feature 2')
plt.legend(loc='best')
plt.title('t-SNE visualization of Iris dataset')
plt.show()
