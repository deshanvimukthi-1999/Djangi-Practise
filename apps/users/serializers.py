from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.users.models import Company, User


class AuthRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            'id', 'first_name', 'last_name', 'email', 'password'
        ]


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'id', 'first_name', 'last_name', 'email', 'password'
        ]