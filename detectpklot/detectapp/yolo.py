from ultralytics import YOLO
from PIL import Image
import cv2
import os
import numpy as np

path = "./detectapp/model_mec/8x_20_kho.onnx"


def predict(image):
    model = YOLO(path)
    im1 = Image.open(image)
    names = model.names
    savedir = "images/"
    results = model.predict(
        source=[im1],
        # conf=0.5,
        save=False,
        show_labels=False,
        show_conf=False,
    )
    count_empty = 0
    count_occupied = 0
    for r in results:
        # print(r)
        for c in r.boxes.cls:
            # print("ccccc:", int(c.item()))
            # print(r.names)
            if r.names[int(c.item())] == "Empty":
                count_empty += 1
            else:
                count_occupied += 1
        boxes = r.boxes.cpu().numpy()
        image_ori = "./images/"
        name_image = os.listdir(image_ori)[0]
        # name_image = "a.jpg"
        path_image = image_ori + name_image  # get boxes on cpu in numpy
        path_image = cv2.imread(path_image)
        boxes = r.boxes.cpu().numpy()  # get boxes on cpu in numpy
        for box in boxes:  # iterate boxes
            b = box.xyxy[0].astype(int)  # get corner points as int
            # print(r)
            # print(box.cls)
            # print(r.names, type(r.names))
            if r.names[int(box.cls)] == "Empty":
                cv2.rectangle(path_image, b[:2], b[2:], (0, 0, 255), 2)
                cv2.imwrite(
                    "./detectapp/static/image_predict/img_predict.png", path_image
                )
            else:
                cv2.rectangle(path_image, b[:2], b[2:], (255, 0, 0), 2)
                cv2.imwrite(
                    "./detectapp/static/image_predict/img_predict.png", path_image
                )
        # print(r.boxes.cls)
        print("complete draw boxes")
    return count_empty, count_occupied


# print(predict("../images/002.png"))
