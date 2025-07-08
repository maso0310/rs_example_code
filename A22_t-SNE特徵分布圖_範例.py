# 匯入繪圖與機器學習相關模組
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.manifold import TSNE
import numpy as np

# 載入內建的鳶尾花 (Iris) 資料集
# X 為 150 筆樣本的 4 維特徵資料（花萼長度、花萼寬度、花瓣長度、花瓣寬度）
# y 為對應的類別標籤（0：Setosa、1：Versicolour、2：Virginica）
iris = datasets.load_iris()
X = iris.data      # 特徵資料 (shape: 150x4)
y = iris.target    # 類別標籤 (shape: 150)

# 建立 t-SNE 模型物件
# n_components=2 表示將原始資料從 4 維降到 2 維
# random_state=42 可確保每次執行結果相同（隨機性固定）
tsne = TSNE(n_components=2, random_state=42)

# 執行降維轉換，得到新的 2 維資料表示
X_tsne = tsne.fit_transform(X)

# 為了繪圖標示不同類別，準備三種顏色對應三種花種
colors = ['red', 'green', 'blue']

# 繪製 t-SNE 降維後的資料點散佈圖
# 使用 enumerate 搭配 np.unique(y)，針對每個類別（0, 1, 2）做標示
for idx, cl in enumerate(np.unique(y)):
    # 不需要的空 plot 呼叫，這一行可以刪除不影響功能
    plt.plot()
    
    # 選取類別為 cl 的樣本，畫出其在降維後的 X-Y 位置
    plt.scatter(
        X_tsne[y == cl, 0],    # X 座標
        X_tsne[y == cl, 1],    # Y 座標
        c=colors[idx],         # 顏色根據類別設定
        label=iris.target_names[cl]  # 圖例標籤（花種名稱）
    )

# 設定圖表標籤與標題
plt.xlabel('t-SNE feature 1')              # X 軸標籤
plt.ylabel('t-SNE feature 2')              # Y 軸標籤
plt.legend(loc='best')                     # 圖例自動擺放在最佳位置
plt.title('t-SNE visualization of Iris dataset')  # 圖表標題

# 顯示圖表
plt.show()
