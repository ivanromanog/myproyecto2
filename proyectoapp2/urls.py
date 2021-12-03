from django.urls import path
from proyectoapp2 import views

urlpatterns = [
    path('',views.index),
]