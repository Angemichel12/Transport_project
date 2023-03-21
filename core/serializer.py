from rest_framework import serializers
from .models import Category,Bus,Transport


class CreateBusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bus
        fields=("code", "name")

class RetriveBusserializer(serializers.ModelSerializer):
    class Meta:
        model=Bus
        fields=("id", "code", "name")
        

class Categoryserializer(serializers.ModelSerializer):
    class Meta: 
        model=Category
        fields= ("id", "name","description")

class TransportModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transport
        fields=("amount","bus","date","Category","description")

