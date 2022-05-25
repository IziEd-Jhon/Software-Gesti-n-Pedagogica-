from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from AppActivity import models

class CustomResouresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resource
        field=[]
        exclude = ()

class CustomFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Folder
        field=[]
        exclude = ()

class CustomArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Archive
        field=[]
        exclude = ()

class CustomActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        field=[]
        exclude = ()

class CustomQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Quiz
        field=[]
        exclude=()

class CustomAssigmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Assigment
        field=[]
        exclude=()