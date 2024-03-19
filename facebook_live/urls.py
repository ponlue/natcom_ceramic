from django.urls import path
from facebook_live import views

urlpatterns = [
    path('', views.fb_live, name='fb-live')
]