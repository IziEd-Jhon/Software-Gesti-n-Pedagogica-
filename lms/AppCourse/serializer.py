from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from AppCourse import models

class CustomCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        field=[
        ]
        exclude = ()

class CustomSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        field = [
        ]
        exclude=()

class CustomSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Section
        field = [            
        ]
        exclude=()