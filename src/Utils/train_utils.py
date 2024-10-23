import json
import os

def load_train_config():
    """ 加載預設訓練設置 """
    config_path = os.path.join(os.path.dirname(__file__), '../configs/train.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

def save_train_config(config):
    """ 保存訓練設置 """
    config_path = os.path.join(os.path.dirname(__file__), '../configs/train.json')
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)

def train_model_with_default_settings(dataset_name):
    """ 使用預設設置進行訓練 """
    config = load_train_config()
    print(f"使用預設設置訓練，資料集: {dataset_name}")
    # 調用 YOLO 訓練代碼
    # 假設這裡有YOLO訓練的邏輯代碼
    print("訓練完成")

def train_model_with_custom_settings(dataset_name, custom_settings):
    """ 使用自定義設置進行訓練 """
    print(f"使用自定義設置訓練，資料集: {dataset_name}")
    config = load_train_config()

    # 更新配置中的設置
    try:
        new_settings = json.loads(custom_settings)  # 解析自定義的 JSON 設置
        config.update(new_settings)
    except json.JSONDecodeError:
        print("無效的 JSON 格式設置")
        return

    # 保存新的配置
    save_train_config(config)

    # 調用 YOLO 訓練代碼
    # 假設這裡有YOLO訓練的邏輯代碼
    print("訓練完成")
