# from rest_framework import serializers
#
#
# class AuthRegisterSerializer(serializers.Serializer):
#     first_name = serializers.CharField(required=True)
#     last_name = serializers.CharField(required=True)
#     email = serializers.CharField(required=True)
#     password = serializers.CharField(required=True)
#     confirm_password = serializers.CharField(required=True)
#
#
# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     email = serializers.CharField(write_only=True)