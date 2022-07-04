from csv import field_size_limit
from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from AppUser import models
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from AppUser.models import customUser
from rest_framework.decorators import api_view

#Crear usuario        
class CustomUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = customUser
            fields = ('username','password','email')
#Hash password 
        def create(self, validated_data):
           user = customUser(**validated_data)
           user.set_password(validated_data['password'])
           user.save()
           return user

class CustomStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customUser
        fields = '__all__'
        
class CustomTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields='__all__'
        #exclude = ['password']
        
class CustomEnrollmentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EnrollmentCourse
        fields='__all__'

class CustomEnrollmentSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EnrollmentSubject
        fields='__all__'

class CustomParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Parent
        fields='__all__'
        # exclude = ('deleted','suspended','firstlogin','lastlogin','lastip','timecreated','timemodified',
        #'is_staff','is_active','is_superuser','last_login','date_joined','groups','user_permissions')

class CustomAnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Annotation
        fields='__all__'
 
class CustomEnrollmentSubject(serializers.ModelSerializer):
    class Meta:
        model = models.EnrollmentSubject
        fields='__all__'

class CustomEnrollmentCourse(serializers.ModelSerializer):
    class Meta:
        model = models.EnrollmentCourse
        fields='__all__'
        
class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
