from django.contrib.auth import get_user_model
from django.template.backends import django
from rest_framework import serializers

from apps.users.models import Company


def create_user(validated_data):
    validated_data.pop('confirm_password')
    validated_data['username'] = validated_data['email']
    instance = get_user_model().objects.create(**validated_data)
    instance.set_password(validated_data['password'])
    instance.save()
    return instance


class AuthRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    company = serializers.CharField(required=False)
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)
    company = CompanySerializer(required=False)

    class Meta:
        model = get_user_model()
        fields = [
            'id', 'first_name', 'last_name', 'email', 'password', 'company', 'phone', 'role'
        ]

    def update(self, instance, validated_data):
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)

        if "email" in validated_data:
            instance.username = validated_data["email"]

        return super().update(instance, validated_data)


