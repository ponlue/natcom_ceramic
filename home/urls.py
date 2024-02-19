from django.urls import include, path
from .views import *
from . import views

app_name = "home"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),# url homepage
    path("potter", views.potter, name="Potter application"), # ceramic app
    path("howto", views.techniquemakingpotter, name="howto"), # ceramic app

]