from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Define source as YouTube video URL
source = "https://www.youtube.com/watch?v=fQfvkym38MM&t=222s"

# Run inference on the source
results = model(source, stream=True)  # generator of Results objects
