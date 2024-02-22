from django.urls import include, path
from .views import *
from . import views

app_name = "home"
urlpatterns = [
    path("", views.HomePageView, name="home"),# url homepage
    path("potter-inventory", views.inventory_of_pottery_making, name="Ceramic application"), # ceramic app
    path("province", views.all_province, name="province"),
    path("potter", views.all_Potter, name="potter"),
    path('post/<int:id>/', views.all_post, name='post'),
    path("contact" , ContactPageView.as_view(), name="home")
]

