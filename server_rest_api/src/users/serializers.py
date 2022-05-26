"""
Project: Fruit Size Estimation
Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:

Use:

"""
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import User, Group


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name",)
