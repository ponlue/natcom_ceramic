from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.HomePageView, name="home"),  # homepage
    path("potter-inventory", views.potter, name="Potter application"),  # ceramic app
    path("howto", views.technique_making_potter_list, name="technique making potter list"),  # test technique_making_potter
    path("province", views.all_province, name="province"),
    path("potter", views.all_Potter, name="potter"),
    path('post/<int:id>/', views.all_post, name='post'),
]
