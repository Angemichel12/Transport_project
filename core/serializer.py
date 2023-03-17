from rest_framework import serializers
from .models import Bus


class Busserializer(serializers.ModelSerializer):
    class Meta:
        model= Bus
        field=("id", "code", "name")
        
       