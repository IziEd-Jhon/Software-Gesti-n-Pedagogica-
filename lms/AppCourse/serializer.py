from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from AppCourse import models

class CustomCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields='__all__'

class CustomSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields='__all__'