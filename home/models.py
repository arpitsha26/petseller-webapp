from django.db import models
from django.contrib.auth.models import User
from .choices import *
import uuid
class Basemodel(models.Model):
    uuid=models.UUIDField(default=uuid.uuid4, primary_key=True,editable=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    class Meta:
        abstract=True

class Category(Basemodel):
    category_name=models.CharField(max_length=100)
    def __str__(self) ->str:
        return self.category_name

class AnimalBreed(Basemodel):
    animal_breed =models.CharField(max_length=100)
    def __str__(self) ->str:
        return self.animal_breed
    
class AnimalColor(Basemodel):
    animal_colour=models.CharField(max_length=100)
    def __str__(self) ->str:
        return self.animal_colour


class Animal(Basemodel):
    animal_owner=models.ForeignKey(User, models.CASCADE, related_name="animals")
    animal_category=models.ForeignKey(Category, models.CASCADE, related_name="category")
    animal_views=models.IntegerField(default=0)
    animal_likes=models.IntegerField(default=1)
    animal_name=models.CharField(max_length=100)
    animal_description=models.TextField()
    animal_slug=models.SlugField(max_length=1000, unique=True)
    animal_gender=models.CharField(max_length=100, choices=GENDER_CHOICES)
    animal_breed=models.ManyToManyField(AnimalBreed)
    animal_colour=models.ManyToManyField(AnimalColor)
    class Meta:
        ordering =['animal_name']
    def __str__(self) ->str:
        return self.animal_name

class AnimalLocation(Basemodel):
    animal=models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="location")
    location=models.CharField(max_length=100)
    def __str__(self) ->str:
        return f'{Animal.animal_name} Location'

class AnimalImages(Basemodel):
    animal=models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="images")
    animals_images=models.ImageField(upload_to="animals")
    def __str__(self) ->str:
        return f'{Animal.animal_name} Images'