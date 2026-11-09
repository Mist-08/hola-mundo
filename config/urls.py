# config/urls.py
from django.contrib import admin
from django.urls import path, include  # nuevo

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("paginas.urls")),  # nuevo
]
