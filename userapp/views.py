from rest_framework.response import Response
from rest_framework.decorators import api_view  
from .models import User    
from .serializers import UserSerializer 
from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    context = {'users_data': serializer.data}

    return render(request, 'users_list.html', context)

@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()   
        return redirect('exito')

    return Response(serializer.errors, status=400) 

@api_view(['POST'])
def create(request):
    name = request.POST.get('name')
    email = request.POST.get('email')

    if name and email:
        url_del_servicio = "https://api-5wbi.onrender.com/users/creation"
        data = {'name': name, 'email': email}

        response = requests.post(url_del_servicio, data=data)
        
        return render(response, 'exito.html')
        
        if response.status_code != 200:
            return render(response, 'users_list.html', {'error_message': 'Error en la solicitud al servicio externo'})

    return render(request, 'users_list.html', {'error_message': 'Nombre y correo electrónico son obligatorios'})

@api_view(['GET'])
def formulario_usuario(request):
    return render(request, 'formulario.html')

def exito(request):
    return render(request, 'exito.html')