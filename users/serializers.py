from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','password', 'email', 'role']
    def validate(self,data):
        if data['username']:
            if CustomUser.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError("Username is taken")
    
        if data['email']:
            if CustomUser.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError("Email is taken")
        return data
    def create(self, validated_data):
        user=CustomUser.objects.create(username=validated_data['username'],email=validated_data['email'],role=validated_data['role'])
        user.set_password(validated_data['password'])
        user.save()
        
        return validated_data 

class TokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls,user):
        token = super(TokenSerializer,cls).get_token(user)

        #custom claims
        token['username'] = user.username
        token['role'] = user.role
        
        return token