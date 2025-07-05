import pandas as pd
# 讀取資料集
df = pd.read_csv('./02_Data/稻穗榖粒含水量調查資料與顏色特徵.csv', low_memory=False)
df = df[(df['HMC']!='Unknow')]

# 特徵數值欄位名稱
X_variable_list = [
    'R','G','B','H1','S1','V1','L2','S2','L','a','b','Y','Cr','Cb','NDI','GI','RGRI','RC','GC','BC','H1C','S1C','V1C','L2C','S2C','LC','aC','bC','YC','CrC','CbC','NDIC','GIC','RGRIC','B_RGB_avg', 'G_RGB_avg', 'W_RGB_avg','B_RGB_R', 'B_RGB_G', 'B_RGB_B','G_RGB_R', 'G_RGB_G', 'G_RGB_B','W_RGB_R', 'W_RGB_G', 'W_RGB_B']

# 標記數值欄位名稱
Y_variable_list = ['HMC']