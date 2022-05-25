from dataclasses import field
from rest_framework import serializers
from AppUser import models

class CustomStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customUser
        fields=[
            'id',
            'username',
            'firstname',
            'lastname',
            'email',
            'birthdate',
            'phonel',
            'phone2',
            'institution',
            'department',
            'address',
            'city',
            'picture',
            'description',
        ]

class CustomTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields=[
            'id',
            'username',
            'firstname',
            'lastname',
            'email',
            'birthdate',
            'phonel',
            'phone2',
            'institution',
            'department',
            'address',
            'city',
            'picture',
            'description',
            'tittles',
            'experience',
            
        ]
class CustomParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Parent
        field=[
            'id'
        ]
