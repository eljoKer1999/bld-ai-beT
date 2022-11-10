from users.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

class RegisteringUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def passwordValidator(self, data):
        if data.get('password1') != data.get('password2'):
            raise serializers.ValidationError("Passwords don't match.")

    
    def emailValidator(self, email):
        existent = User.objects.filter(email=email).first()
        if existent:
            raise serializers.ValidationError("Email is already in use")
        return email

class getUserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "bio")