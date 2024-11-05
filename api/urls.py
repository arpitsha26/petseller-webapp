from django.contrib import admin
from django.urls import include, path
from home.views import *

urlpatterns = [
   path('animals/', AnimalView.as_view() )
]