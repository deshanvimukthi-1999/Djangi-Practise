from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.users.models import Company


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

    def update(self, instance, validated_data):
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)

        if "email" in validated_data:
            instance.username = validated_data["email"]

        return super().update(instance, validated_data)
