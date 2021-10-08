from django.contrib.auth import get_user_model
from django.template.backends import django
from rest_framework import serializers

from apps.users.models import Company, User


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'Email': ' email already exits '})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ' username already exits '})

        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


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


