from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
import os
import subprocess
from .yolo import predict
# Create your views here.
def home(request):
    return render(request, "home.html",)



# Create your views here.


def hotel_image_view(request):

	if request.method == 'POST':
		form = HotelForm(request.POST, request.FILES)
		dir = './images/'
		for f in os.listdir(dir):
			os.remove(os.path.join(dir, f))
		if form.is_valid():
			form.save()
			return redirect('success')
	else:
		form = HotelForm()
	return render(request, 'home.html', {'form': form})


def success(request):
	path = "./images/"
	image = os.listdir(path)[0]
	path_image = path + image
	print(path_image)
	count = predict(path_image)
	# subprocess.run([os.remove(path_image)]) 
	return HttpResponse("trống {} có xe {}".format(count[0],count[1]))
