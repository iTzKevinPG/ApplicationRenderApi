from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUsers),
    path('create', views.addUser),
    path('formulario', views.formulario_usuario),
    path('exito', views.exito),
    path('add_user/', views.addUser, name='add_user'),
]