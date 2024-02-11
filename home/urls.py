from django.urls import path
from .views import *
from . import views

app_name = "home"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),# url homepage
    path("ceramic-app", views.ceramic_app, name="Ceramic application"), # ceramic app
    path("blog-single-page", views.BlogPageView, name="BlogPageView"),
]