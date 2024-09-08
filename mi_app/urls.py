from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_mensaje, name='mostrar_mensaje'),
]
