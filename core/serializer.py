from rest_framework import serializers
from .models import Category,Bus

class Busserializer(serializers.ModelSerializer):
    class Meta:
        model= Bus
        field=("id", "code", "name")

class Categoryserializer(serializers.ModelSerializer):
    class meta: 
        model=Category
        fields= ("id", "name","description")



