from django.shortcuts import render
from .models import juego,consola,figura
from .serializers import juegoSerializer, consolaSerializer, figuraSerializer

##creacion api
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
#autenticacion
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#Vistas de el sitio web:
def index(request):
    juegos = juego.objects.all()
    return render(request, 'core/index.html', {'juegos':juegos})
@csrf_exempt
@api_view
#@permission_classes((IsAuthenticated,))
def lista_juego(request):
    if request.method =='GET':
        query=juego.objects.all()
        serializer=juegoSerializer(query, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        seriazer=juegoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST) 

def lista_consola(request):
    if request.method =='GET':
        query=juego.objects.all()
        serializer=consolaSerializer(query, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer=consolaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
def lista_figura(request):
    if request.method =='GET':
        query=figura.objects.all()
        serializer=figuraSerializer(query, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer=figuraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))

def detalle_juego(request,id):
    try:
        juegos = juego.objects.get(nombre=id)  
    except juego.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serilizer = juegoSerializer(juegos)
        return Response(serilizer.data)
    if request.method == 'PUT':
        serializer = juegoSerializer(juegos,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response(serilizer.errors,status=status.HTTP_404_NOT_FOUND)

    if request.method =='DELETE':
        juegos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)       
    
def detalle_consola(request,id):
    try:
        consolas = consola.objects.get(nombre=id)
    except consola.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serilizer = consolaSerializer(consolas)
        return Response(serilizer.data)
    if request.method == 'PUT':
        serializer = consolaSerializer(consolas,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response(serilizer.errors,status=status.HTTP_404_NOT_FOUND)
    if request.method =='DELETE':
        consolas.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
def detalle_figura(request,id):

    try:
        figuras = figura.objects.get(nombre=id)
    except figura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serilizer = figuraSerializer(figuras)
        return Response(serilizer.data)
    if request.method == 'PUT':
        serializer = figuraSerializer(figura,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response(serilizer.errors,status=status.HTTP_404_NOT_FOUND)
    if request.method =='DELETE':
        figuras.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    


@api_view(['POST'])
def login(request):
    data =JSONParser().parse(request)
    username=data['username']
    password=data['password']

    try:
        user=User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Nombre de usuario no existe")
    
    pass_valida= check_password(password, user.password)

    if not pass_valida:
        return Response("Password Incorrecto")
    
    token, created = Token.objects.get_or_create(user=user)

    return Response(token.key)

    