from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Bus,Category
from core.serializer import Categoryserializer,  Busserializer
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



@api_view(['GET'])
def categories_list(request):
        if request.method == 'GET':
            categories = Category.objects.all()
            serializer = Categoryserializer(categories, many=True)
            return Response(serializer.data)
@api_view(['GET'])
def categories_details(request,id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Categoryserializer(category)
        return Response(serializer.data)