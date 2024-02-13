from django.urls import path
from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "home"
urlpatterns = [
    path("home", HomePageView.as_view(), name="home"),# url homepage
    path("ceramic-app", views.ceramic_app, name="Ceramic application"), # ceramic app
    path("kompot-page",views.KompotPageView, name="Kompot traditional ceramic"),
]