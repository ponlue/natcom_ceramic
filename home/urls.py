from django.urls import include, path
from .views import *
from . import views

app_name = "home"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),# url homepage
    path("potter-inventory", views.potter_inventory, name="Ceramic application"), # ceramic app
]