from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Bus
from core.serializer import Busserializer
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def Bus_list(request,format=None):
    if request.method =='GET':
        all_Bus = Bus.objects.all()
        serializer = Busserializer(all_Bus, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def Bus_detail(request,id, format=None):
    try:
        Buses = Bus.object.get(pk=id)
    except Bus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Busserializer(Buses)
        return Response(serializer.data)