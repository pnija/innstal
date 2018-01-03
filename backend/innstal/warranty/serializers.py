from rest_framework.serializers import ModelSerializer
from .models import Warranty
from product.models import UserProfile


class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = UserProfile
        exclude = ['user_type', 'avatar', ]


class WarrantyApplicationSerializer(ModelSerializer):
    user = UserProfileSerializer(many=False)

    class Meta:
        model = Warranty
        fields = '__all__'

    def create(self, validated_data):
        profile_data = validated_data.pop('user')
        warranty = Warranty.objects.create(**validated_data)
        profile_datas, created = UserProfile.objects.get_or_create(user=profile_data['user'])
        profile_datas.phone = profile_data["phone"]
        profile_datas.address = profile_data["address"]
        profile_datas.city = profile_data["city"]
        profile_datas.state = profile_data["state"]
        profile_datas.country = profile_data["country"]
        profile_datas.save()
        warranty.user = profile_datas
        warranty.save()
        return warranty

