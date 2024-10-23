def get_dataset_path(dataset_name):
    # 構建資料集路徑
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Datasets'))
    dataset_path = os.path.join(base_path, dataset_name, 'data.yaml')
    
    # 檢查 data.yaml 是否存在
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"資料集配置文件 {dataset_path} 不存在！")
    
    return dataset_path
