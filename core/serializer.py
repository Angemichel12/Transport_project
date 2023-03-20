from rest_framework import serializers
from .models import Category

class categoryserializer(serializers.ModelSerializer):
    class meta: 
        model=Category
        fields= ("id", "name","description")

