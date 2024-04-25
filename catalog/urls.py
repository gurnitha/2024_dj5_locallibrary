# src/catalog/urls.py

from django.urls import path

# Locals
from . views import home_view

# namespace
app_name = "catalog"

urlpatterns = [
    path("", home_view, name="home"),
]