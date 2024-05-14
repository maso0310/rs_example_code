import joblib 
import pandas as pd
from sklearn.metrics import mean_absolute_error

# 讀取資料集
df = pd.read_csv('./02_Data/稻穗榖粒含水量調查資料與顏色特徵.csv')
df = df[(df['HMC']!='Unknow')]

# 特徵數值欄位名稱
X_variable_list = [
    'R','G','B','H1','S1','V1','L2','S2','L','a','b','Y','Cr','Cb','NDI','GI','RGRI','RC','GC','BC','H1C','S1C','V1C','L2C','S2C','LC','aC','bC','YC','CrC','CbC','NDIC','GIC','RGRIC','B_RGB_avg', 'G_RGB_avg', 'W_RGB_avg','B_RGB_R', 'B_RGB_G', 'B_RGB_B','G_RGB_R', 'G_RGB_G', 'G_RGB_B','W_RGB_R', 'W_RGB_G', 'W_RGB_B',
]

# 標記數值欄位名稱
Y_variable_list = ['HMC']

# 讀取特徵與標記資料
image_name_list = df['image_name'].values
X = df[X_variable_list].values
Y = df[Y_variable_list].values

# 建立空的dictionary存放輸出資料集
predictions = {}
# 將原有的檔案名稱列表存入
predictions['image_name'] = image_name_list
# 將原有的標記資料數值扁平化之後存入
predictions['Truth'] = Y.flatten()

# 讀取訓練好的模型
# 依照模型名稱建立迴圈
for model_name in ['rf', 'mlp', 'svr', 'mlr']:
    # 讀取指定模型
    model = joblib.load(f'./04_Model_saved/{model_name}.pkl')
    # 進行預測
    prediction = model.predict(X).flatten()
    # 將預測結果加入dictionary
    predictions[model_name] = prediction
    # 計算MAE
    MAE = round(mean_absolute_error(Y, prediction), 2)
    print(f'{model_name} MAE: {MAE}')

# 將predictions轉換成Dataframe
df = pd.DataFrame(predictions)
df.to_csv('./03_Result/CSV/Model_Predictions.csv', encoding='utf-8')