from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # homepage
    path("potter", views.potter, name="Potter application"),  # ceramic app
    path("howto", views.technique_making_potter_list, name="technique making potter list"),  # test technique_making_potter
    path('success-submitted', views.success_submitted_potter_form)
]
