from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]