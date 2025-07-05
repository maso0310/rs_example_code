from C01_設定檔 import *
from C02_模型儲存 import *
from sklearn.svm import SVR
from adapt.instance_based import IWC
from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import mean_absolute_error
import numpy as np

# 源領域與目標領域指定
source_df = df[(df['Period']!=1121) & (df['Period']!=1122)]
target_df = df[(df['Period']==1121) | (df['Period']==1122)]
target_df = target_df.sample(100)

# 特徵資料萃取
Xs = source_df[X_variable_list].values
Xt = target_df[X_variable_list].values

# 標記資料萃取
ys = source_df[Y_variable_list].values.astype(np.float32)
yt = target_df[Y_variable_list].values.astype(np.float32)

model = IWC(SVR(kernel='rbf',C=1000,gamma='scale',epsilon=0.1), classifier=RidgeClassifier(0.), Xt=Xt, random_state=42)

model.fit(Xs, ys)

# 模型預測
predictions = model.predict(Xt)
MAE = mean_absolute_error(yt, predictions)
print(f'MAE: {MAE:.2f}')

save_model(model, 'IWC')