from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUsers),
    path('creation', views.addUser),
    path('formulario', views.formulario_usuario),
    path('exito/', views.exito, name='exito'),
    path('create/', views.create, name='create'),
]