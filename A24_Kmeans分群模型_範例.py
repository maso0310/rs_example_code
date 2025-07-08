# 匯入繪圖模組與資料集、KMeans 模型
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

# 載入 scikit-learn 內建的鳶尾花 (Iris) 資料集
# X 為 150 筆樣本的 4 維特徵資料（花萼長度、花萼寬度、花瓣長度、花瓣寬度）
# y 為真實標籤（此處不使用，只為參考）
iris = datasets.load_iris()
X = iris.data      # 特徵資料 (shape: 150x4)
y = iris.target    # 類別標籤 (shape: 150)

# 初始化 K-Means 模型，設定要分成 3 群（因為鳶尾花有三種品種）
kmeans = KMeans(n_clusters=3, random_state=42)

# 使用 KMeans 模型擬合整個資料集
# 模型會嘗試將資料點分配到 3 個群集，並找出各群的中心點
kmeans.fit(X)

# 根據訓練好的模型，對原始資料預測其所屬的群集標籤
# labels 會是每個樣本的群集編號（0、1 或 2）
labels = kmeans.predict(X)

# 將聚類結果可視化（僅以第 1、2 維特徵進行 2D 繪圖：花萼長度、花萼寬度）
# 使用顏色區分不同群集，邊框設為黑色讓點更明顯
plt.scatter(
    X[:, 0],         # X 軸：花萼長度 (sepal length)
    X[:, 1],         # Y 軸：花萼寬度 (sepal width)
    c=labels,        # 根據 KMeans 預測的群集標籤上色
    cmap='viridis',  # 色彩映射樣式
    edgecolor='k'    # 黑色邊框
)

# 擷取模型的聚類中心（centroids），shape: (3, 4)
centers = kmeans.cluster_centers_

# 將聚類中心以紅色透明圓點顯示，讓群集中心更醒目
plt.scatter(
    centers[:, 0],   # 中心點的花萼長度
    centers[:, 1],   # 中心點的花萼寬度
    c='red',         # 顏色設為紅色
    s=200,           # 點的大小
    alpha=0.5        # 透明度
)

# 設定圖表標題與座標軸標籤
plt.title('K-means clustering on Iris dataset')  # 圖表標題
plt.xlabel('Sepal length')                      # X 軸標籤
plt.ylabel('Sepal width')                       # Y 軸標籤

# 顯示圖表
plt.show()
