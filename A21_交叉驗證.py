# 從設定檔匯入變數，例如：df, X_variable_list, Y_variable_list
from C01_設定檔 import *

# 匯入必要模組
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, train_test_split
import warnings

# 忽略 sklearn 可能產生的警告（例如收斂警告），避免干擾輸出畫面
warnings.filterwarnings("ignore")

# 將資料集切分為訓練資料與測試資料（此處僅對訓練資料做交叉驗證）
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# 擷取特徵與目標欄位的值
X = train_df[X_variable_list].values  # 特徵矩陣（多欄）
Y = train_df[Y_variable_list].values.ravel()  # 目標欄位（扁平化為一維）

# 建立四種模型（超參數已設定）
rf_model = RandomForestRegressor(n_estimators=1000, max_depth=3, random_state=42)
mlp_model = MLPRegressor(solver='lbfgs', hidden_layer_sizes=(30, 30), learning_rate='adaptive', max_iter=200, epsilon=0.001)
svr_model = SVR(kernel='rbf', C=1000, gamma='scale', epsilon=0.1)
mlr_model = LinearRegression()

# 使用四種模型進行交叉驗證評估（以 MAE 為指標）
for model_name in ['rf', 'mlp', 'svr', 'mlr']:
    # 執行 K-fold 交叉驗證（cv=5 表示將訓練資料切為 5 等份，每次用 1 份驗證，其餘 4 份訓練）
    # scoring='neg_mean_absolute_error' 表示以「負的 MAE」來計算（scikit-learn 越大越好，負數是為了相容）
    scores = cross_val_score(
        eval(f'{model_name}_model'),  # 使用模型變數名稱，例如 rf_model
        X, Y,
        cv=5,
        scoring='neg_mean_absolute_error'
    )

    # 顯示每次交叉驗證的 MAE 分數（取負號變回正值）
    print("交叉驗證分數:", -scores)

    # 顯示平均 MAE（越小代表預測誤差越小）
    print("平均分數:", -scores.mean())
