from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Warranty


class WarrantyApplicationSerializer(ModelSerializer):
    email = serializers.EmailField(max_length=255)
    phone = serializers.CharField(max_length=15)
    class Meta:
        model = Warranty
        fields = '__all__'
