from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from AppActivity import models

class CustomResouresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resource
        field=[]
        exclude = ()