from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User

class UserTokenSerializer(serializers.ModelSerializer):
        class Meta:
            model= User
            fields =('username','email','first_name','last_name')