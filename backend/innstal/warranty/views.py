from django.core.mail import send_mail
from collections import OrderedDict
from django.db import IntegrityError
from rest_framework import status, viewsets
from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_countries.data import COUNTRIES

from product.models import Product
from product.serializers import ProductSerializer
from .models import COMPANY_CHOICES, ClaimedWarranty
from .models import Warranty, UserProfile
from .serializers import WarrantyApplicationSerializer, UserProfileSerializer, ClaimedWarrantySerializer


# Create your views here.


class WarrantApplicationViewSet(ModelViewSet):
    queryset = Warranty.objects.all()
    serializer_class = WarrantyApplicationSerializer

    def create(self, request, *args, **kwargs):
        import pdb;pdb.set_trace()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        user_profile_data, created = UserProfile.objects.get_or_create(user=user)
        user_profile_data.phone = serializer.validated_data.get('user_profile').get('phone')
        user_profile_data.user.email = serializer.validated_data.get('user_profile').get('user').get('email')
        user_profile_data.address = serializer.validated_data.get('user_profile').get('address')
        user_profile_data.city = serializer.validated_data.get('user_profile').get('city')
        user_profile_data.state = serializer.validated_data.get('user_profile').get('state')
        user_profile_data.country = serializer.validated_data.get('user_profile').get('country')
        user_profile_data.save()
        serializer.save(user_profile=user_profile_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChoicesListViewSet(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        country_list = [{'code': key, 'label': value} for key, value in OrderedDict(COUNTRIES).items()]
        company_choices = [{'code': key, 'label': value}for key, value in OrderedDict(COMPANY_CHOICES).items()]
        print(company_choices)
        choice_dict = {"countries": country_list, "companies": company_choices}
        return Response(choice_dict, 200)


class UserProfileView(ModelViewSet):
    http_method_names = ['get','PUT']
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(email=user_profile_data)


class ClaimWarrantyViewSet(ModelViewSet):
    queryset = ClaimedWarranty.objects.all()
    serializer_class = ClaimedWarrantySerializer
    response = {}

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        user_profile = UserProfile.objects.get(user=user)
        warranty = Warranty.objects.get(warranty=kwargs)
        serializer.save(user_profile=user_profile, warranty=warranty)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



