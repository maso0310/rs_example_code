# 匯入繪圖模組與 PCA 降維工具
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA

# 載入 scikit-learn 內建的鳶尾花（Iris）資料集
# X：特徵資料（150 筆樣本 × 4 個特徵）
# y：目標類別（0: Setosa, 1: Versicolour, 2: Virginica）
iris = datasets.load_iris()
X = iris.data      # shape = (150, 4)
y = iris.target    # shape = (150,)

# 初始化 PCA 模型，設定將特徵資料降至 2 維
pca = PCA(n_components=2)

# 執行 PCA 降維操作，回傳轉換後的 2 維資料
X_pca = pca.fit_transform(X)  # shape = (150, 2)

# 開始繪製降維後的散佈圖
plt.figure(figsize=(8, 6))  # 設定圖表大小為 8x6 吋

# 使用 scatter 畫出所有資料點，依據目標類別 y 設定不同顏色
# cmap='viridis' 表示使用漸層色系，c 對應類別，edgecolor 為邊框色
scatter = plt.scatter(
    X_pca[:, 0],      # 第一主成分（橫軸）
    X_pca[:, 1],      # 第二主成分（縱軸）
    c=y,              # 顏色對應類別 y
    cmap='viridis',   # 使用 viridis 漸層色系
    edgecolor='k',    # 黑色邊框讓點更明顯
    s=50              # 點的大小
)

# 設定圖表標題與軸標籤
plt.title('PCA of Iris Dataset')               # 圖表標題
plt.xlabel('Principal Component 1')            # X 軸名稱
plt.ylabel('Principal Component 2')            # Y 軸名稱

# 加入顏色圖例（colorbar），標註顏色對應的類別
plt.colorbar(scatter, label='Species')         # 右側顏色對應說明

# 顯示圖表
plt.show()
