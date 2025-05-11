from django.urls import path
from .views import buscar_clima

urlpatterns = [
    path('', buscar_clima, name='buscar_clima'),
]