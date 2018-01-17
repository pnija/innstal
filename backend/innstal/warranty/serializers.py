import re
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Warranty, ClaimedWarranty
from product.models import UserProfile
from .models import Warranty
from product.models import UserProfile, ProductType


class UserProfileSerializer(ModelSerializer):

    email = serializers.EmailField(source='user.email')
    username = serializers.CharField(source='user.username')

    class Meta:
        model = UserProfile
        fields = ['email', 'username', 'phone', 'address', 'city', 'state', 'country', 'id']

    def validate(self, data):
        match = re.search("\d{10}", data['phone'])
        if not match:
            raise serializers.ValidationError("Invalid Number")
        return data


class WarrantyApplicationSerializer(ModelSerializer):
    # user = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()

    class Meta:
        model = Warranty
        exclude = ()

    # def get_user(self,instance):
    #     if instance.user_profile.user is not None:
    #         return instance

    def get_email(self, instance):
        print(instance.user_profile)
        if instance.user_profile is not None:
            return instance.user_profile.user.email

    def get_username(self, instance):
        if instance.user_profile is not None:
            return instance.user_profile.user.username

    def get_phone(self, instance):
        if instance.user_profile is not None:
            return instance.user_profile.phone

    def get_address(self, instance):
        if instance.user_profile is not None:
            return instance.user_profile.address

    def get_city(self, instance):
        if instance.user_profile is not None:
            import pdb;pdb.set_trace()
            return instance.user_profile.city.name

    def get_state(self, instance):
        if instance.user_profile is not None:
            return instance.user_profile.state.name

    def get_country(self, instance):
        if instance.user_profile is not None:
            return instance.user_profile.country.name

class ClaimedWarrantySerializer(ModelSerializer):
    # user_profile = UserProfileSerializer()
    # warranty = WarrantyApplicationSerializer()

    class Meta:
        model = ClaimedWarranty
        fields = '__all__'


