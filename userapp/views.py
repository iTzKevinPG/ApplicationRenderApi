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
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()   
        return Response(serializer.data, status=201) 

    return Response(serializer.errors, status=400) 

def formulario_usuario(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        if name and email:
            url_del_servicio = "https://api-5wbi.onrender.com/users/create"  
            data = {'name': name, 'email': email}

            try:
                response = requests.post(url_del_servicio, data=data)
                response.raise_for_status()
                return render(request, 'exito.html')
            except requests.exceptions.RequestException as e:
                print(f"Error al conectar con el servidor: {e}")
                return render(request, 'exito.html')

    return render(request, 'formulario.html')

def exito(request):
    return render(request, 'exito.html')