from C01_設定檔 import *
from C02_模型儲存 import *
from adapt.feature_based import DANN
from sklearn.metrics import mean_absolute_error
import numpy as np

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 隱藏警告和錯誤信息，只顯示致命錯誤

# 源領域與目標領域指定
source_df = df[(df['Period']!=1121) & (df['Period']!=1122)]
target_df = df[(df['Period']==1121) | (df['Period']==1122)]
target_df = target_df.sample(100)
print(f'源領域形狀: {source_df.shape}')
print(f'目標領域形狀: {target_df.shape}')

# 特徵資料萃取
Xs = source_df[X_variable_list].values
Xt = target_df[X_variable_list].values

# 標記資料萃取
ys = source_df[Y_variable_list].values.astype(np.float32)
yt = target_df[Y_variable_list].values.astype(np.float32)

# DANN模型訓練 lambda 預設為 0.1 Xt為目標領域特徵
model = DANN(lambda_=0.1, Xt=Xt, metrics=["mae"], random_state=42)

# 模型訓練
model.fit(Xs, ys, epochs=100, verbose=0)

# 模型預測
predictions = model.predict(Xt)
MAE = mean_absolute_error(yt, predictions)
print(f'MAE: {MAE:.2f}')

save_model(model, 'DANN')