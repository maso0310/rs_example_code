# 匯入設定檔（df, X_variable_list, Y_variable_list 等資料變數）
from C01_設定檔 import *

# 匯入模型儲存功能
from C02_模型儲存 import *

# 匯入回歸模型：SVR（支援向量迴歸）
from sklearn.svm import SVR

# 匯入 ADAPT 套件中的 IWC 模型（Instance Weighting based domain adaptation）
from adapt.instance_based import IWC

# 匯入分類器（用於 IWC 計算樣本權重）：RidgeClassifier 為 L2 正則化分類器
from sklearn.linear_model import RidgeClassifier

# 匯入評估指標與陣列處理工具
from sklearn.metrics import mean_absolute_error
import numpy as np

# -------------------------------
# 定義源領域與目標領域資料集
# -------------------------------

# 將非 1121/1122 的期作視為源領域（source domain）
source_df = df[(df['Period'] != 1121) & (df['Period'] != 1122)]

# 將 1121 或 1122 期作視為目標領域（target domain），並隨機取樣 100 筆
target_df = df[(df['Period'] == 1121) | (df['Period'] == 1122)]
target_df = target_df.sample(100)

# -------------------------------
# 萃取特徵與標記資料
# -------------------------------

# 特徵資料（X）
Xs = source_df[X_variable_list].values  # 源領域特徵
Xt = target_df[X_variable_list].values  # 目標領域特徵

# 標記資料（Y），轉為 float32 格式以避免警告或錯誤
ys = source_df[Y_variable_list].values.astype(np.float32)
yt = target_df[Y_variable_list].values.astype(np.float32)

# -------------------------------
# 初始化並訓練 IWC 模型
# -------------------------------

# 建立 IWC 模型（Instance Weighting Classifier）
# 使用 SVR 作為回歸器（regressor）
# 使用 RidgeClassifier 來計算樣本的領域轉換權重
# Xt 為目標領域特徵（用於估算權重）
model = IWC(
    SVR(kernel='rbf', C=1000, gamma='scale', epsilon=0.1),  # 回歸模型
    classifier=RidgeClassifier(0.),                         # 權重計算用分類器（0 代表不加正則化）
    Xt=Xt,
    random_state=42
)

# 訓練模型：會自動根據分類器計算每個樣本的領域相似性作為加權依據，並訓練 SVR 模型
model.fit(Xs, ys)

# -------------------------------
# 模型預測與評估
# -------------------------------

# 預測目標領域的 Y 值
predictions = model.predict(Xt)

# 計算預測結果與真實值的 MAE（平均絕對誤差）
MAE = mean_absolute_error(yt, predictions)
print(f'MAE: {MAE:.2f}')

# -------------------------------
# 儲存模型
# -------------------------------

# 將訓練好的模型儲存起來（自定義函式）
save_model(model, 'IWC')
