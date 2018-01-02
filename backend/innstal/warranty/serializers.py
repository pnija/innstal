from rest_framework.serializers import ModelSerializer
from .models import Warranty


class WarrantyApplicationSerializer(ModelSerializer):
    class Meta:
        model = Warranty
        fields = '__all__'
