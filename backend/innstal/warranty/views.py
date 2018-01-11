from django.core.mail import send_mail
from django.db import IntegrityError
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Warranty, UserProfile
from .serializers import WarrantyApplicationSerializer, UserProfileSerializer

# Create your views here.


class WarrantApplicationViewSet(ModelViewSet):
    queryset = Warranty.objects.all()
    serializer_class = WarrantyApplicationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        try:
            user_profile_data, created = UserProfile.objects.get_or_create(user=user)
            user_profile_data.phone = serializer.validated_data.get('user_profile').get('phone')
            user_profile_data.user.email = serializer.validated_data.get('user_profile').get('user').get('email')
            user_profile_data.address = serializer.validated_data.get('user_profile').get('address')
            user_profile_data.city = serializer.validated_data.get('user_profile').get('city')
            user_profile_data.state = serializer.validated_data.get('user_profile').get('state')
            user_profile_data.country = serializer.validated_data.get('user_profile').get('country')
            user_profile_data.save()
            serializer.save(user_profile=user_profile_data)
        except IntegrityError:
            print ('No user')
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserProfileView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
