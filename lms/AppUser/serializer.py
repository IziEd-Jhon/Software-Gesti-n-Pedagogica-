from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from AppUser import models

class CustomStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customUser
        #fields='__all__'
        exclude = ['password']

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
        ]
        exclude = ()
        # exclude = ('deleted','suspended','firstlogin','lastlogin','lastip','timecreated','timemodified',
        #'is_staff','is_active','is_superuser','last_login','date_joined','groups','user_permissions')

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()