from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
import os
import subprocess
import shutil
from .yolo import predict
from .log import data, print_log


# Create your views here.
def home(request):
    return render(
        request,
        "home.html",
    )


# Create your views here.


def hotel_image_view(request):
    if request.method == "POST":
        form = HotelForm(request.POST, request.FILES)
        dir = "./images/"
        selected_file = request.POST.get("selected_file")
        log = "============" + "Đã chọn model: " + selected_file + "============"
        data(log)
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        if os.path.exists("./detectapp/static/runs/"):
            shutil.rmtree("./detectapp/static/runs/")
        if form.is_valid():
            form.save()
            return redirect("success", selected_file=selected_file)

    else:
        form = HotelForm()
    folder_path = "./detectapp/model_mec/"  # Đường dẫn tới thư mục chứa các file

    file_list = []  # Danh sách chứa tên các file

    # Lặp qua các file trong thư mục
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_list.append(filename)
    # file_list = ["file1.txt", "file2.txt", "file3.txt"]
    return render(request, "home.html", {"form": form, "file_list": file_list})


def success(request, selected_file):
    path = "./images/"
    image = os.listdir(path)[0]
    path_image = path + image
    log = "============" + "Image need predict: " + path_image + "============"
    data(log)
    count = predict(path_image, selected_file)
    # count = (1, 1)
    # path_img_pre = r"../images/img_predict.png"
    # os.system("pwd")
    # print("image predicted: ", path_img_pre)
    context = {"empty": count[0], "car": count[1]}
    # print(path_img_pre)}
    return render(request, "show_image.html", context)
