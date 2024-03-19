from django.urls import path
from facebook_live import views

urlpatterns = [
    path('', views.live, name='fb-live')
]