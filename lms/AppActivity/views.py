from ast import Sub
from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import *
from AppActivity.serializer import *

# Vista generica de Recursos
class ResourceList(generics.CreateAPIView):
    queryset= Resource.objects.all()
    serializer_class = CustomResouresSerializer
    permission_classes=[permissions.IsAuthenticated]

class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Resource.objects.all()
    serializer_class=CustomResouresSerializer
    permission_classes=[permissions.IsAuthenticated]