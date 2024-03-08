from django.urls import path
from .views import index


urlpatterns = [
    path('generate', index, name='generate_qr_code'),
]
