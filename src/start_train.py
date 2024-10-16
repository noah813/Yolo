from ultralytics import YOLO


model = YOLO("yolo11n.yaml")
model = YOLO("yolo11n.pt")
model = YOLO("yolo11n.yaml").load("yolo11n.pt")


print("Enter data path:")
data = input()
results = model.train(data=data, epochs=100, imgsz=640, cache=True, device=0, )
