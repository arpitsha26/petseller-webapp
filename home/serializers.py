from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class meta:
        model=Category
        fields= ['category_name',]
        
class AnimalBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model=AnimalBreed
        fields=['animal_breed']
class AnimalColorSerializer(serializers.ModelSerializer):
    class Meta:
        model=AnimalColor
        fields='__all__'
class AnimalSerializer(serializers.ModelSerializer):
    animal_category= serializers.SerializerMethodField()
    animal_colour=AnimalColorSerializer(many= True)
    def get_animal_category(self,obj):
        return obj.animal_category.category_name
    
    # def to_representation(self, instance):
    #     payload={
    #         'animal_category' : instance.animal_category.category_name,
    #         'animal_likes': instance.animal_likes,
    #         'animal_views' : instance.animal_views,
    #         'animal_name' : instance.animal_name,
    #         'animal_description': instance.animal_description,            
    #     }
    #     return payload
    
    class Meta:
        model=Animal
        exclude=['updated_at']
class AnimalLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=AnimalLocation
        fields='__all__'
class AnimalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=AnimalImages
        fields='__all__'