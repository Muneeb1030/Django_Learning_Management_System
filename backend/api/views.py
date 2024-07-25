from django.shortcuts import render
from api import serializers as api_serializers
from rest_framework_simplejwt.views import TokenObtainPairView

class UserTOPView(TokenObtainPairView):
    serializer_class = api_serializers.UserTOPSerializer
    
