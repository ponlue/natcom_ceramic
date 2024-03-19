from django.urls import path
from potter2 import views

urlpatterns = [
    path('', views.potter2, name='potter2')
]