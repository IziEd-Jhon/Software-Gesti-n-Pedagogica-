from rest_framework import serializers
from AppUser import models

class PostCustomUser(serializers.ModelSerializer):
    class Meta:
        model = models.customUser
        fields=[
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