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

# 特徵數值欄位名稱
X_variable_list = [
    'R','G','B','H1','S1','V1','L2','S2','L','a','b','Y','Cr','Cb','NDI','GI','RGRI',
    'RC','GC','BC','H1C','S1C','V1C','L2C','S2C','LC','aC','bC','YC','CrC','CbC','NDIC','GIC','RGRIC',
    'B_RGB_avg', 'G_RGB_avg', 'W_RGB_avg',
    'B_RGB_R', 'B_RGB_G', 'B_RGB_B',
    'G_RGB_R', 'G_RGB_G', 'G_RGB_B',
    'W_RGB_R', 'W_RGB_G', 'W_RGB_B',
]

# 標記數值欄位名稱
Y_variable_list = ['HMC']

# 讀取與切割訓練/測試資料集
file_name = '稻穗榖粒含水量調查資料與顏色特徵.csv'
df = pd.read_csv(f'./02_Data/{file_name}')
df = df[(df['HMC']!='Unknow')].sample(1000)
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# 讀取訓練與測試的特徵資料
train_X = train_df[X_variable_list].values
test_X = test_df[X_variable_list].values

# 讀取訓練與測試的標記資料
train_Y = train_df[Y_variable_list].values
test_Y = test_df[Y_variable_list].values

# 建立模式與設定參數
rf_model = RandomForestRegressor(n_estimators=1000, max_depth = 3, random_state=42)
mlp_model = MLPRegressor(solver='lbfgs',hidden_layer_sizes=(30,30),learning_rate='adaptive',max_iter=200,epsilon=0.001)
svr_model = SVR(kernel='rbf',C=1000,gamma='scale',epsilon=0.1)
mlr_model = LinearRegression()

# 模型訓練
rf_model.fit(train_X,train_Y.flatten())
mlp_model.fit(train_X,train_Y.flatten())
svr_model.fit(train_X,train_Y.flatten())
mlr_model.fit(train_X,train_Y.flatten())

# 模型預測
rf_predictions = rf_model.predict(test_X)
mlp_predictions = mlp_model.predict(test_X)
svr_predictions = svr_model.predict(test_X)
mlr_predictions = mlr_model.predict(test_X)

# 儲存模型
os.makedirs('./04_Model_saved', exist_ok=True)
for model_name in ['rf', 'mlp', 'svr', 'mlr']:
    joblib.dump(eval(f'{model_name}_model'), f'./04_Model_saved/{model_name}.pkl')

# 結果摘要
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


# 繪製圖表
model_names = ['rf', 'mlp', 'svr', 'mlr']
colors = ['red', 'green', 'blue', 'orange']
for model_name, clr in zip(model_names, colors):
    plt.figure(figsize=(6, 6))
    plt.scatter(test_Y, eval(f'{model_name}_predictions'), label=model_name, color=clr)
    plt.plot([0, 60], [0, 60], 'k--', lw=2, label='1:1 Line')
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title(model_name.upper(), fontsize=20)
    plt.savefig(f'./03_Result/Figsure/{model_name}.jpg')
    plt.clf()