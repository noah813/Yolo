from ultralytics import YOLO


model = YOLO("yolo11n.yaml")
model = YOLO("yolo11n.pt")
model = YOLO("yolo11n.yaml").load("yolo11n.pt")


results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
