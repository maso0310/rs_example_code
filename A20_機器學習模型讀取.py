# 匯入必要套件
import joblib 
import pandas as pd
from sklearn.metrics import mean_absolute_error

# 讀取原始資料集（稻穗顏色與含水率資料）
df = pd.read_csv('./02_Data/稻穗榖粒含水量調查資料與顏色特徵.csv')

# 移除 HMC 欄位為 'Unknow' 的資料（不能作為目標值進行預測）
df = df[(df['HMC'] != 'Unknow')]

# 特徵數值欄位名稱：顏色空間、色彩統計與植生指標等特徵
X_variable_list = [
    'R','G','B','H1','S1','V1','L2','S2','L','a','b','Y','Cr','Cb','NDI','GI','RGRI',
    'RC','GC','BC','H1C','S1C','V1C','L2C','S2C','LC','aC','bC','YC','CrC','CbC','NDIC','GIC','RGRIC',
    'B_RGB_avg', 'G_RGB_avg', 'W_RGB_avg',
    'B_RGB_R', 'B_RGB_G', 'B_RGB_B',
    'G_RGB_R', 'G_RGB_G', 'G_RGB_B',
    'W_RGB_R', 'W_RGB_G', 'W_RGB_B',
]

# 標記數值欄位名稱（目標變數）：含水率（Harvest Moisture Content）
Y_variable_list = ['HMC']

# 從資料集中擷取欄位資料
image_name_list = df['image_name'].values  # 圖像名稱列表（作為識別用）
X = df[X_variable_list].values             # 特徵資料
Y = df[Y_variable_list].values             # 目標資料（含水率）

# 建立空的字典，準備儲存預測結果
predictions = {}

# 將圖像檔名加入預測結果中，作為識別標籤
predictions['image_name'] = image_name_list

# 將真實的 HMC 數值（扁平化成一維）加入預測結果中
predictions['Truth'] = Y.flatten()

# 使用已訓練好的四種模型進行預測：rf（隨機森林）、mlp（多層感知器）、svr（支援向量回歸）、mlr（線性回歸）
for model_name in ['rf', 'mlp', 'svr', 'mlr']:
    # 從指定路徑讀取模型檔案（joblib 格式）
    model = joblib.load(f'./04_Model_saved/{model_name}.pkl')
    
    # 對整份資料進行預測，並將結果轉為一維陣列
    prediction = model.predict(X).flatten()
    
    # 將每個模型的預測結果加入 predictions 字典，以模型名稱為 key
    predictions[model_name] = prediction
    
    # 計算模型的 MAE（平均絕對誤差），並列印結果
    MAE = round(mean_absolute_error(Y, prediction), 2)
    print(f'{model_name} MAE: {MAE}')

# 將完整預測結果轉為 DataFrame 格式
df = pd.DataFrame(predictions)

# 儲存為 CSV 檔案，包含 image_name、Truth、四種模型預測欄位
df.to_csv('./03_Result/CSV/Model_Predictions.csv', encoding='utf-8')
