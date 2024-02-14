from django.urls import include, path
from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "home"
urlpatterns = [
    path("home", HomePageView.as_view(), name="home"),# url homepage
    path("ceramic-app", views.ceramic_app, name="Ceramic application"), # ceramic app
    path("kompot-page",views.KompotPageView, name="Kompot traditional ceramic"),
    path("", HomePageView.as_view(), name="home"),# url homepage
    # path("potter-inventory", views.inventory_of_pottery_making, name="Ceramic application"),
    path("kampot", views.kampot_view, name="Ceramic kampot page"), # kampot page
]