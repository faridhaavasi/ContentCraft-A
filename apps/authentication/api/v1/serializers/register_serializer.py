from rest_framework import serializers
from django.contrib.auth import get_user_model

user = get_user_model()

class SteponeRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('Password and Confirm Password does not match')
        return data

    def create(self, validated_data):
        user.objects.create_user(email=validated_data['email'], password=validated_data['password'])
        return validated_data
