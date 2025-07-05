import os
import traceback
import joblib

def save_model(model, model_name):
    try:
        os.makedirs(f'./04_Model_saved/{model_name}', exist_ok=True)
        model.save(f'./04_Model_saved/{model_name}')
    except:
        if os.path.isdir(f'./04_Model_saved/{model_name}')==True:
            os.rmdir(f'./04_Model_saved/{model_name}')
        # To save a model
        joblib.dump(model, f'./04_Model_saved/{model_name}')