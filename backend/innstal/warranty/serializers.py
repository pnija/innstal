import re
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Warranty, ClaimedWarranty
from product.models import UserProfile


class UserProfileSerializer(ModelSerializer):
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = UserProfile
        fields = ['email', 'phone', 'address', 'city', 'state', 'country']

    def validate(self, data):
        match = re.search("\d{10}", data['phone'])
        if not match:
            raise serializers.ValidationError("Invalid Number")
        return data


class WarrantyApplicationSerializer(ModelSerializer):
    user_profile = UserProfileSerializer()

    class Meta:
        model = Warranty
        fields = '__all__'

class ClaimedWarrantySerializer(ModelSerializer):
    # user_profile = UserProfileSerializer()
    warranty = WarrantyApplicationSerializer()

    class Meta:
        model = ClaimedWarranty
        fields = '__all__'


