from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import  Category
from core.serializer import Categoryserializer
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def Bus_list(request,format=None):
    if request.method =='GET':
        all_Bus = Category.objects.all()
        serializer = Categoryserializer(all_Bus, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def Bus_detail(request,id, format=None):
    try:
        categories = Category.object.get(pk=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Categoryserializer(categories)
        return Response(serializer.data)