from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Warranty
from product.models import UserProfile


class UserProfileSerializer(ModelSerializer):
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = UserProfile
        fields = ['email', 'phone', 'address', 'city', 'state', 'country',]


class WarrantyApplicationSerializer(ModelSerializer):
    user_profile = UserProfileSerializer()

    class Meta:
        model = Warranty
        fields = '__all__'


