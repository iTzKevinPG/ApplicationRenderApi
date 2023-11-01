from rest_framework.response import Response
from rest_framework.decorators import api_view  
from .models import User    
from .serializers import UserSerializer 

# Create your views here.

# Obtener todos los usuarios
@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# Obtener un solo usuario por ID
@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

# Agregar un usuario
@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()   
        return Response(serializer.data, status=201)  # Devuelve 201 Created en caso de éxito

    return Response(serializer.errors, status=400)  # Devuelve errores de validación en caso de fallo

# Actualizar un usuario
@api_view(['PUT'])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()   
        return Response(serializer.data)

    return Response(serializer.errors, status=400)

# Eliminar un usuario
@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()

    return Response('User(s) deleted', status=204)  # Devuelve 204 No Content en caso de éxito
