from ultralytics import YOLO
from PIL import Image


path = "./detectapp/mec_1.pt"

def predict(image):
    model = YOLO(path)
    im1 = Image.open(image)
    names = model.names
    savedir="./runs/detect/"
    results = model.predict(source=[im1],save=True,conf=0.35, project=savedir)
    count_empty = 0
    count_occupied = 0
    for r in results:
        for c in r.boxes.cls:
            if names[int(c)] == "Empty":
                count_empty +=1
            else:
                count_occupied+=1
    return count_empty,count_occupied
# print(predict("../images/002.png"))
