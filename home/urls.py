from django.urls import path
from .views import *
from . import views

app_name = "home"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    ]