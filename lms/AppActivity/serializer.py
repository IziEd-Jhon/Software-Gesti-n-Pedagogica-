from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from AppActivity import models

class CustomResouresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resource
        fields='__all__'

class CustomFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Folder
        fields='__all__'

class CustomArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Archive
        fields='__all__'

class CustomActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields='__all__'

class CustomQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Quiz
        fields='__all__'

class CustomAssigmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Assigment
        fields='__all__'