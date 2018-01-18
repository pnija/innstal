import re
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, exceptions
from rest_framework.generics import get_object_or_404
from rest_framework.validators import UniqueValidator
from common.models import UserProfile, Newsletter, City, State, Country, Blog, BusinessUserProfile, UserPlans


# class UserProfileSerializer(serializers.ModelSerializer):
#     user_id = serializers.IntegerField(source='user.id', read_only = True)
#     first_name = serializers.CharField(source = 'user.first_name')
#     last_name = serializers.CharField(source = 'user.last_name')
#     email = serializers.CharField(source = 'user.email')
#
#     class Meta:
#         model = UserProfile
#         fields = ('user_id', 'first_name', 'last_name', 'email', 'phone', 'user_type', 'avatar')
#

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
    )

    username = serializers.CharField()
    password = serializers.CharField(min_length=8, required=False, allow_null=True)
    phone = serializers.CharField(source='userprofile.phone', required=False)
    dob = serializers.DateField(source='userprofile.dob', required=False)
    avatar = serializers.ImageField(source='userprofile.avatar', required=False, allow_null=True)

    def validate_email(self, value):
        request = self.context.get('request')
        if User.objects.filter(email=value).exists():
            if request.user.email != value:
                raise serializers.ValidationError('Email needs to be unique')
        return value

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                            validated_data['email'],
                                            validated_data['password'])
        user.is_active = False
        user.save()
        self.fields.pop('password')
        profile = UserProfile(user=user)
        userprofile = validated_data['userprofile']
        profile.phone = userprofile['phone']
        # profile.address = userprofile['address']
        profile.dob = userprofile['dob']
        try:
            profile.avatar = userprofile['avatar']
        except:
            pass
        profile.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email',  'password', 'phone', 'dob', 'avatar')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all(), required=False, allow_null=True)
    state = serializers.PrimaryKeyRelatedField(queryset=State.objects.all(), required=False, allow_null=True)
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), required=False, allow_null=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'phone', 'user_type', 'avatar', 'address', 'user', 'dob', 'city', 'country', 'state', 'zipcode')

    def update(self, instance, validated_data):
        user_id = instance.user_id
        user_data = validated_data.pop('user')
        user = User.objects.get(pk=user_id)
        user.email = user_data['email']
        user.username = user_data['username']
        try:
            user.set_password(user_data['password'])
        except:
            pass
        user.save()
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.zipcode = validated_data.get('zipcode', instance.zipcode)
        instance.save()
        return instance

class BusinessAccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    state = serializers.PrimaryKeyRelatedField(queryset=State.objects.all())
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())

    class Meta:
        model = BusinessUserProfile
        fields = ('id','phone','user_type','avatar','address',
                  'company_name', 'person_to_contact',
                  'fax_number','user','city','state','country')

    def create(self, validated_data):
        user = validated_data.pop('user')
        user_data = User.objects.create_user(user['username'],
                                             user['email'],
                                             user['password'])
        user_data.is_active = False
        user_data.save()
        profile = BusinessUserProfile(user=user_data)
        profile.address = validated_data['address']
        profile.company_name = validated_data['company_name']
        profile.city = validated_data['city']
        profile.state = validated_data['state']
        profile.country = validated_data['country']
        try:
            profile.avatar = validated_data['avatar']
        except:
            pass
        profile.save()
        return profile



class ContactSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    message = serializers.CharField()

    def validate_phone(self, value):

        if re.match(r'^(?:\+)?(\d{10,16})$',value):
            return value

        raise serializers.ValidationError("Invalid Phone Number")


class NewsletterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    is_subscribed = serializers.BooleanField()

    def create(self, validated_data):
        newsletter = Newsletter.objects.create(**validated_data)
        return newsletter

    def update(self, instance, validated_data):
        instance.is_subscribed = validated_data.get('is_subscribed', instance.is_subscribed)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    class Meta:
        model = Newsletter
        fields = ('id', 'email','is_subscribed')


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value

class UpdatePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)


class BlogSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only = True)
    first_name = serializers.CharField(source = 'user.user.first_name')
    last_name = serializers.CharField(source = 'user.user.last_name')
    username = serializers.CharField(source = 'user.user.username')

    class Meta:
        model = Blog
        fields = ('id', 'user_id', 'first_name', 'last_name', 'username', 'blog_title',\
                  'blog_subtitle', 'blog_image', 'blog_content')

class UserPlanSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    plan_id = serializers.IntegerField(source='plan.id')


    class Meta:
        model = UserPlans
        fields = ('id', 'user_id', 'plan_id')
