from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class meta:
        model=Category
        fields='__all__'
class AnimalBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model=AnimalBreed
        fields='__all__'
class AnimalColorSerializer(serializers.ModelSerializer):
    class Meta:
        model=AnimalColor
        fields='__all__'
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Animal
        fields='__all__'
class AnimalLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=AnimalLocation
        fields='__all__'
class AnimalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=AnimalImages
        fields='__all__'