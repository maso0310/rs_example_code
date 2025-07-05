from C01_設定檔 import *
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")

# 分割訓練資料集與測試資料集
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# 讀取特徵與標記資料
X = train_df[X_variable_list].values
Y = train_df[Y_variable_list].values.ravel()

# 建立模式與設定參數
rf_model = RandomForestRegressor(n_estimators=1000, max_depth = 3, random_state=42)
mlp_model = MLPRegressor(solver='lbfgs',hidden_layer_sizes=(30,30),learning_rate='adaptive',max_iter=200,epsilon=0.001)
svr_model = SVR(kernel='rbf',C=1000,gamma='scale',epsilon=0.1)
mlr_model = LinearRegression()

# 依據模型名稱建立迴圈
for model_name in ['rf', 'mlp', 'svr', 'mlr']:
    # 執行交叉驗證
    # cv參數定義了交叉驗證的次數
    scores = cross_val_score(eval(f'{model_name}_model'), X, Y, cv=5, scoring='neg_mean_absolute_error')

    # 輸出結果
    print("交叉驗證分數:", -scores)
    print("平均分數:", -scores.mean())
