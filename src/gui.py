import tkinter as tk
from tkinter import messagebox
from utils import get_dataset_path
from train_utils import train_model

# 創建主界面
def create_gui():
    root = tk.Tk()
    root.title("YOLO 訓練介面")
    
    # 資料集名稱
    tk.Label(root, text="資料集名稱").grid(row=0, column=0)
    dataset_name_entry = tk.Entry(root)
    dataset_name_entry.grid(row=0, column=1)
    
    # 訓練模式選擇
    var = tk.IntVar()
    var.set(0)
    tk.Radiobutton(root, text="使用預設設置", variable=var, value=0).grid(row=1, column=0)
    tk.Radiobutton(root, text="自定義設置", variable=var, value=1).grid(row=1, column=1)

    # 自定義設置的參數輸入框
    tk.Label(root, text="訓練輪數").grid(row=2, column=0)
    epochs_entry = tk.Entry(root)
    epochs_entry.grid(row=2, column=1)

    tk.Label(root, text="批次大小").grid(row=3, column=0)
    batch_size_entry = tk.Entry(root)
    batch_size_entry.grid(row=3, column=1)

    tk.Label(root, text="學習率").grid(row=4, column=0)
    learning_rate_entry = tk.Entry(root)
    learning_rate_entry.grid(row=4, column=1)

    # 開始訓練按鈕
    def on_start_button_click():
        dataset_name = dataset_name_entry.get().strip()
        if var.get() == 0:  # 使用預設設置
            start_training(dataset_name)
        else:  # 使用自定義設置
            epochs = int(epochs_entry.get().strip() or "10")
            batch_size = int(batch_size_entry.get().strip() or "16")
            learning_rate = float(learning_rate_entry.get().strip() or "0.001")
            start_training(dataset_name, custom_settings=True, epochs=epochs, batch_size=batch_size, learning_rate=learning_rate)

    start_button = tk.Button(root, text="開始訓練", command=on_start_button_click)
    start_button.grid(row=5, column=0, columnspan=2)

    # 退出按鈕
    exit_button = tk.Button(root, text="退出", command=root.quit)
    exit_button.grid(row=6, column=0, columnspan=2)

    root.mainloop()
