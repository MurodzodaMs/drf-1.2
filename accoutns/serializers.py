from rest_framework import serializers
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class meta:
        model = CustomUser
        fields = ('username','email', 'password', 'confirm_password')

    def validate(self, attrs):
        password = attrs['password']
        password2 = attrs['confirm_password']
        if not password == password2:
            raise serializers.ValidationError("passwords do not match")
        return super().validate(attrs)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data)
        return user