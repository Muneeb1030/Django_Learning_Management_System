from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from userauths.models import User, ProfileUser

class UserTOPSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['full_name'] = user.full_name
        token['email'] = user.email
        token['username'] = user.username
        
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = '__all__'