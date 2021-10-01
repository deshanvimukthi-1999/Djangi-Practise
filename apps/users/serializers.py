from rest_framework import serializers

from apps.users.models import Company, User


class AuthRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    company_type = serializers.ChoiceField(choices=CompanyTypes.choices,required=True)
    company_name = serializers.CharField(required=False)
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'password', 'company', 'phone', 'role'
        ]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

