from rest_framework import serializers
<<<<<<< HEAD
from .models import Bus

class CreateBusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bus
        fields=("code", "name")

class RetriveBusserializer(serializers.ModelSerializer):
    class Meta:
        model=Bus
        fields=("id", "code", "name")
        
       
=======
from .models import Category,Bus

class Busserializer(serializers.ModelSerializer):
    class Meta:
        model= Bus
        field=("id", "code", "name")

class Categoryserializer(serializers.ModelSerializer):
    class meta: 
        model=Category
        fields= ("id", "name","description")



>>>>>>> 3dbab3a1656f40f6d4e387c165d65d60132c0dfa
