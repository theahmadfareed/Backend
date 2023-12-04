from django.contrib import admin
from django.urls import path, include
from myapp.views import *     

urlpatterns = [
    path("admin/", admin.site.urls),
    path("fetch_save_data/", fetch_save_data, name="fetch_save_data"),
    path("", display_data, name="display_data"),
    path("signUp", signUp, name="signUp"),
    path("signIn", signIn, name="signIn"),
    path('api/', include('myapp.urls')),
]