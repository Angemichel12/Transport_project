from rest_framework import serializers
from .models import Category,Bus


class CreateBusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bus
        fields=("code", "name")

class RetriveBusserializer(serializers.ModelSerializer):
    class Meta:
        model=Bus
        fields=("id", "code", "name")
        

class Categoryserializer(serializers.ModelSerializer):
    class meta: 
        model=Category
        fields= ("id", "name","description")

