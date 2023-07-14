from django.urls import path, re_path
from detectapp import views
from .views import *


urlpatterns = [
    # path('', views.home),
    path("", hotel_image_view, name="image_upload"),
    path("success/<str:selected_file>/", success, name="success"),
]
