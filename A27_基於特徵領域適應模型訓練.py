# 匯入自定義模組：C01_設定檔 包含 df、X_variable_list、Y_variable_list 等變數
from C01_設定檔 import *

# 匯入模型儲存函式（自定義的 save_model 函數）
from C02_模型儲存 import *

# 匯入 ADAPT 套件中的 DANN 模型（用於領域適應）
from adapt.feature_based import DANN

# 匯入評估指標與陣列處理工具
from sklearn.metrics import mean_absolute_error
import numpy as np

# 設定環境變數：讓 TensorFlow 執行時只顯示錯誤，不顯示警告與提示訊息
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# -----------------------
# 分離源領域與目標領域資料
# -----------------------

# 將 1121 與 1122 期作作為「目標領域」
target_df = df[(df['Period'] == 1121) | (df['Period'] == 1122)].sample(100)  # 隨機取樣 100 筆
# 其餘期作作為「源領域」
source_df = df[(df['Period'] != 1121) & (df['Period'] != 1122)]

# 顯示兩個領域的資料筆數與欄位數
print(f'源領域形狀: {source_df.shape}')
print(f'目標領域形狀: {target_df.shape}')

# -----------------------
# 萃取特徵資料與標記資料
# -----------------------

# 源領域特徵與目標領域特徵（X）
Xs = source_df[X_variable_list].values  # shape = (源樣本數, 特徵數)
Xt = target_df[X_variable_list].values  # shape = (目標樣本數, 特徵數)

# 源領域標記與目標領域標記（Y），並轉換成 float32 格式
ys = source_df[Y_variable_list].values.astype(np.float32)
yt = target_df[Y_variable_list].values.astype(np.float32)

# -----------------------
# 建立並訓練 DANN 模型
# -----------------------

# 建立 DANN 模型物件
# lambda_：控制對抗損失的權重（越高越強調領域對抗）
# Xt：目標領域特徵（供模型學習領域不變性）
# metrics：設定評估指標
model = DANN(lambda_=0.1, Xt=Xt, metrics=["mae"], random_state=42)

# 使用源領域資料訓練模型，epoch=100，verbose=0 表示不顯示訓練過程
model.fit(Xs, ys, epochs=100, verbose=0)

# -----------------------
# 預測與誤差評估
# -----------------------

# 對目標領域資料做預測
predictions = model.predict(Xt)

# 計算 MAE（Mean Absolute Error 平均絕對誤差）
MAE = mean_absolute_error(yt, predictions)
print(f'MAE: {MAE:.2f}')  # 輸出 MAE 到小數點第 2 位

# -----------------------
# 儲存訓練好的模型
# -----------------------

# 儲存模型至指定檔名（會呼叫自定義的 save_model 函式）
save_model(model, 'DANN')
