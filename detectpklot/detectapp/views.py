from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
import os
import subprocess
import shutil
from .yolo import predict


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
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        if os.path.exists("./detectapp/static/runs/"):
            shutil.rmtree("./detectapp/static/runs/")
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = HotelForm()
    return render(request, "home.html", {"form": form})


def success(request):
    path = "./images/"
    image = os.listdir(path)[0]
    path_image = path + image
    print("image need predict: ", path_image)
    count = predict(path_image)
    # path_img_pre = r"../images/img_predict.png"
    # os.system("pwd")
    path_img_pre = "./static/image_predict/img_predict.png"
    print("image predicted: ", path_img_pre)
    # subprocess.run([os.remove(path_image)])
    context = {"empty": count[0], "car": count[1], "image": path_img_pre}
    # print(path_img_pre)}
    return render(request, "show_image.html", context)
