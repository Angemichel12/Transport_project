from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Bus
from core.serializer import RetriveBusserializer, CreateBusSerializer
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def Bus_list(request,format=None):
    if request.method=='GET':
        all_Bus = Bus.objects.all()
        serializer = RetriveBusserializer(all_Bus, many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=CreateBusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET','PUT','DELETE'])
def Bus_detail(request, id):
    try:
        Buses = Bus.objects.get(pk=id)
    except Bus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RetriveBusserializer(Buses)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CreateBusSerializer(Buses, data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Buses.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    