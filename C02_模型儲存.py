# 匯入必要模組
import os           # 用來建立資料夾與檢查檔案狀態
import traceback    # 可用來追蹤錯誤細節（此程式中未用到，但通常搭配 except 使用）
import joblib       # 用來儲存 scikit-learn 類型的模型（序列化工具）

# ----------------------------------------
# 函式名稱：save_model
# 功能：根據模型的類型，自動儲存模型至指定資料夾
# model      ：已訓練好的模型物件
# model_name ：儲存時的資料夾名稱（會存到 ./04_Model_saved/model_name）
# ----------------------------------------
def save_model(model, model_name):
    try:
        # 建立模型儲存的資料夾（若不存在就建立，若已存在不報錯）
        os.makedirs(f'./04_Model_saved/{model_name}', exist_ok=True)

        # 嘗試使用 `.save()` 儲存模型
        # 如果是 ADAPT 套件中的模型（例如 DANN、IWC 等），支援 model.save()
        model.save(f'./04_Model_saved/{model_name}')

    except:
        # 若上面的 model.save() 發生錯誤（多數 sklearn 模型無此方法）
        # 則進入 except 區塊，改用 joblib 方式儲存模型

        # 如果先前成功建立了資料夾但失敗，則先刪除該資料夾（避免殘留空資料夾）
        if os.path.isdir(f'./04_Model_saved/{model_name}') == True:
            os.rmdir(f'./04_Model_saved/{model_name}')

        # 使用 joblib.dump 儲存模型至 .pkl 檔案
        # 適用於 sklearn 的 SVR、RandomForest、MLPRegressor 等模型
        joblib.dump(model, f'./04_Model_saved/{model_name}')
