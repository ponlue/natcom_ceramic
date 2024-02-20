from django.urls import include, path
from .views import *
from . import views

app_name = "home"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),# url homepage
    path("ceramic-app", views.ceramic_app, name="Ceramic application"), # ceramic app
    path("kampot", views.kampot_view, name="Ceramic kampot page"), # kampot page
]