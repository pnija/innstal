from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, exceptions
from rest_framework.generics import get_object_or_404
from rest_framework.validators import UniqueValidator

from common.models import UserProfile, Newsletter

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('phone','user_type','avatar')


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)
    phone = serializers.CharField(source='userprofile.phone', required=False)
    dob = serializers.DateField(source='userprofile.dob', required=False)
    avatar = serializers.ImageField(source='userprofile.avatar', required=False)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        self.fields.pop('password')
        profile = UserProfile(user=user)
        userprofile = validated_data['userprofile']
        profile.phone = userprofile['phone']
        profile.dob = userprofile['dob']
        try:
            profile.avatar = userprofile['avatar']
        except:
            pass
        profile.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'dob', 'password','phone','avatar')


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

    def validate_new_password(self, value):
        validate_password(value)
        return value




