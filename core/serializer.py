from rest_framework import serializers
from .models import Bus

class CreateBusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bus
        fields=("code", "name")

class RetriveBusserializer(serializers.ModelSerializer):
    class Meta:
        model=Bus
        fields=("id", "code", "name")
        
       