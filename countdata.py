import os
from glob import glob
import random
import shutil
YoloFolder = "/PKLotYoloData/"
SubDirs = ["UFPR04/Sunny/", "UFPR04/Rainy/", "UFPR04/Cloudy/", "UFPR05/Sunny/", "UFPR05/Rainy/", "UFPR05/Cloudy/", "PUCPR/Sunny/","PUCPR/Rainy/", "PUCPR/Cloudy/"]
# SubDirs = ["PUCPR/Cloudy/"]
train_txt = "./train.txt"
val_txt = "./val.txt"
percentage_train = 90

data_list = {
    "train": [],
    "valid": []
}
train_dir = "./train_data/images/train/"
train_dir_lable = "./train_data/labels/train/"
val_dir = "./train_data/images/val/"
val_dir_lable = "./train_data/labels/val/"
def appendData(_images, type):
    for img in _images:
        data_list[type].append(img)

for _folder in SubDirs:
    folder =  "."+ YoloFolder + "HasXML/" + _folder
    dir_content = [d for d in os.listdir(os.path.join(folder)) if os.path.isdir(os.path.join(folder,d))]
    for d in dir_content:
        folder_path = os.path.join(folder,d)
        images = glob(os.path.join(folder_path, "*.jpg"))
        txt = []
            # images = images[i].replace(".jpg",".txt")
        # txt = glob(os.path.join(folder_path, "*.txt"))
        random.shuffle(images)
        txt_err = []
        for i in range(len(images)):
            file_txt =images[i].replace(".jpg",".txt")
            if os.path.isfile(file_txt):
                txt.append(file_txt)
            else:
                txt_err.append(images[i])
        images = [file for file in images if file not in txt_err]
        total = len(images)
        train_data_amount = round(total / 100 * percentage_train)
        train_data = images[:train_data_amount]
        train_data_txt = txt[:train_data_amount]
        # print("------------------")
        # print(train_data)
        # print(train_data_txt)
        for file in train_data:
            shutil.copy2(file,train_dir)
        for file in train_data_txt:
            shutil.copy2(file,train_dir_lable)
        appendData(train_data, "train")
        if len(train_data) < total:
            val_data = images[train_data_amount:]
            val_data_txt = txt[train_data_amount:]
            for file in val_data:
                shutil.copy2(file, val_dir)
            for file in val_data_txt:
                shutil.copy2(file, val_dir_lable)
            appendData(val_data, "valid")

SubDirs = ["data_them"]
for _folder in SubDirs:
    folder =  "."+ YoloFolder + "HasXML/" + _folder
    dir_content = [d for d in os.listdir(os.path.join(folder)) if os.path.isdir(os.path.join(folder,d))]
    for d in dir_content:
        folder_path = os.path.join(folder,d)
        images = glob(os.path.join(folder_path, "*.jpg"))
        txt = []
            # images = images[i].replace(".jpg",".txt")
        # txt = glob(os.path.join(folder_path, "*.txt"))
        random.shuffle(images)
        for i in range(len(images)):
            txt.append(images[i].replace(".jpg",".txt"))
        total = len(images)
        train_data_amount = round(total / 100 * 100)
        train_data = images[:train_data_amount]
        train_data_txt = txt[:train_data_amount]
        # print("------------------")
        # print(train_data)
        # print(train_data_txt)
        for file in train_data:
            shutil.copy2(file,train_dir)
        for file in train_data_txt:
            shutil.copy2(file,train_dir_lable)
        appendData(train_data, "train")
with open(train_txt, 'w') as outfile:
    outfile.write("\n".join(data_list["train"]))
with open(val_txt, 'w') as outfile:
    outfile.write("\n".join(data_list["valid"]))