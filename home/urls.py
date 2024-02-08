from django.urls import include, path
from .views import *
from . import views

app_name = "home"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),# url homepage
    path("inventory_of_pottery_maker", views.inventory_of_pottery_making, name="Ceramic application"), # ceramic app
    path("kampot", views.kampot_view, name="Ceramic kampot page"), # kampot page
]