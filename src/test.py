
import cv2
import torch

# 設定模型路徑和檢測閾值
model_path = "best.pt"  # 替換為你的 YOLO 模型權重路徑
confidence_threshold = 0.3

# 載入 YOLO 模型
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

# 開啟影像或影片（攝影機）
cap = cv2.VideoCapture(0)  # 0 表示使用攝影機；或替換成影片檔路徑

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO 檢測
    results = model(frame)

    # 取得檢測結果
    detections = results.pandas().xyxy[0]  # 使用 Pandas DataFrame 格式取得結果

    for index, row in detections.iterrows():
        if row['confidence'] > confidence_threshold:
            # 取得邊界框座標
            x_min, y_min, x_max, y_max = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
            # 計算中心座標
            center_x, center_y = (x_min + x_max) // 2, (y_min + y_max) // 2

            # 畫出邊界框和中心點
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
            cv2.putText(frame, f"({center_x}, {center_y})", (center_x, center_y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # 顯示影像
    cv2.imshow("YOLO Detection", frame)

    # 按下 'q' 鍵退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放攝影機並關閉視窗
cap.release()
cv2.destroyAllWindows()
