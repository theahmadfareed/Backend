from django.contrib import admin
from django.urls import path, include
from myapp.views import *     

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("fetch_save_data/", fetch_save_data, name="fetch_save_data"),
    path("display_data/", display_data, name="display_data"),
]