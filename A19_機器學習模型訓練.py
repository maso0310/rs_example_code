# 匯入必要的套件
import os
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import joblib

# 指定要使用的特徵欄位（X 變數），包含多種顏色空間與植生指標的數值特徵
X_variable_list = [
    'R','G','B','H1','S1','V1','L2','S2','L','a','b','Y','Cr','Cb','NDI','GI','RGRI',
    'RC','GC','BC','H1C','S1C','V1C','L2C','S2C','LC','aC','bC','YC','CrC','CbC','NDIC','GIC','RGRIC',
    'B_RGB_avg', 'G_RGB_avg', 'W_RGB_avg',
    'B_RGB_R', 'B_RGB_G', 'B_RGB_B',
    'G_RGB_R', 'G_RGB_G', 'G_RGB_B',
    'W_RGB_R', 'W_RGB_G', 'W_RGB_B',
]

# 指定目標欄位（Y 變數）：含水率 HMC（Harvest Moisture Content）
Y_variable_list = ['HMC']

# 設定資料來源檔名
file_name = '稻穗榖粒含水量調查資料與顏色特徵.csv'

# 讀取資料，並排除 'HMC' 欄位為 'Unknow' 的資料，接著隨機抽樣 1000 筆以加快訓練速度
df = pd.read_csv(f'./02_Data/{file_name}')
df = df[(df['HMC']!='Unknow')].sample(1000)

# 切分為訓練資料（80%）與測試資料（20%），並固定亂數種子確保可重現性
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# 從訓練與測試資料中擷取特徵欄位（X）
train_X = train_df[X_variable_list].values
test_X = test_df[X_variable_list].values

# 從訓練與測試資料中擷取目標欄位（Y）
train_Y = train_df[Y_variable_list].values
test_Y = test_df[Y_variable_list].values

# 建立四種迴歸模型：
# RandomForest：使用 1000 棵樹、最大深度 3
# MLP：雙層隱藏層，每層 30 個神經元，lbfgs 優化器，自動學習率，最多訓練 200 次
# SVR：使用 RBF 核心，C=1000，epsilon=0.1
# 線性回歸：預設參數
rf_model = RandomForestRegressor(n_estimators=1000, max_depth = 3, random_state=42)
mlp_model = MLPRegressor(solver='lbfgs',hidden_layer_sizes=(30,30),learning_rate='adaptive',max_iter=200,epsilon=0.001)
svr_model = SVR(kernel='rbf',C=1000,gamma='scale',epsilon=0.1)
mlr_model = LinearRegression()

# 訓練四種模型，將資料對應到目標變數（使用 .flatten() 是因為 Y 是 2D array）
rf_model.fit(train_X,train_Y.flatten())
mlp_model.fit(train_X,train_Y.flatten())
svr_model.fit(train_X,train_Y.flatten())
mlr_model.fit(train_X,train_Y.flatten())

# 預測測試資料的結果
rf_predictions = rf_model.predict(test_X)
mlp_predictions = mlp_model.predict(test_X)
svr_predictions = svr_model.predict(test_X)
mlr_predictions = mlr_model.predict(test_X)

# 儲存四種模型為 .pkl 檔案，方便未來載入使用
os.makedirs('./04_Model_saved', exist_ok=True)
for model_name in ['rf', 'mlp', 'svr', 'mlr']:
    joblib.dump(eval(f'{model_name}_model'), f'./04_Model_saved/{model_name}.pkl')

# 顯示訓練與測試資料的基本資訊，以及四種模型的 MAE（平均絕對誤差）結果
print(f'''
訓練資料集: {file_name}
訓練資料數量: {train_df.shape}
測試資料數量: {test_df.shape}

特徵欄位名稱: {X_variable_list}
標記欄位名稱: {Y_variable_list}

RF MAE: {mean_absolute_error(test_Y, rf_predictions):.2f}
MLP MAE: {mean_absolute_error(test_Y, mlp_predictions):.2f}
SVR MAE: {mean_absolute_error(test_Y, svr_predictions):.2f}
MLR MAE: {mean_absolute_error(test_Y, mlr_predictions):.2f}
''')

# 設定模型名稱與對應顏色，用於後續繪圖
model_names = ['rf', 'mlp', 'svr', 'mlr']
colors = ['red', 'green', 'blue', 'orange']

# 繪製每一種模型的預測結果與實際值對比圖（散佈圖），並與 1:1 理想線比較
for model_name, clr in zip(model_names, colors):
    plt.figure(figsize=(6, 6))  # 設定圖表大小
    plt.scatter(test_Y, eval(f'{model_name}_predictions'), label=model_name, color=clr)  # 實際 vs 預測
    plt.plot([0, 60], [0, 60], 'k--', lw=2, label='1:1 Line')  # 理想線
    plt.xlabel('Actual Values')  # X 軸標籤
    plt.ylabel('Predicted Values')  # Y 軸標籤
    plt.title(model_name.upper(), fontsize=20)  # 圖表標題（模型名稱大寫）
    plt.savefig(f'./03_Result/Figsure/{model_name}.jpg')  # 儲存為圖檔
    plt.clf()  # 清除圖表以便下一輪繪製
