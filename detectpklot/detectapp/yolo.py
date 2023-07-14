from ultralytics import YOLO
from PIL import Image
import cv2
import os
import numpy as np
from .log import data, print_log

path1 = "./detectapp/model_mec/"


def predict(image, model_name):
    path = path1 + model_name
    model = YOLO(path)
    im1 = Image.open(image)
    names = model.names
    savedir = "images/"
    log = (
        "============" + "Thực hiện predict bằng model: " + model_name + "============"
    )
    data(log)
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
                cv2.imwrite("./detectapp/static/image/img_predict.png", path_image)
            else:
                cv2.rectangle(path_image, b[:2], b[2:], (255, 0, 0), 2)
                cv2.imwrite("./detectapp/static/image/img_predict.png", path_image)
        # print(r.boxes.cls)
        log = "============" + "Complete draw boxes" + "============"
        data(log)
        print_log()

    return count_empty, count_occupied


# print(predict("../images/002.png"))
