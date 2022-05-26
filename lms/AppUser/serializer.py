from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from AppUser import models

class CustomStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customUser
        fields='__all__'
        
class CustomTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
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
        