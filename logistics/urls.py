from django.urls import path, include
from .views import paquete_detail

urlpatterns = [
    path('paquetes/<str:tracking>/', paquete_detail, name='paquete_detail'),
]