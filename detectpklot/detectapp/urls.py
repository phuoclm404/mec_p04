from django.urls import path , re_path
from detectapp import views
from .views import *


urlpatterns = [ 
    path('', views.home),
    path('image_upload', hotel_image_view, name='image_upload'),
    path('success', success, name='success'),
]