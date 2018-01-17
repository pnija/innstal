from collections import OrderedDict
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_countries.data import COUNTRIES
from .models import COMPANY_CHOICES
from common.models import Country, City, State
from .models import Warranty, UserProfile, ProductType
from .serializers import WarrantyApplicationSerializer, UserProfileSerializer

# Create your views here.


class WarrantApplicationViewSet(ModelViewSet):
    # parser_classes = (FileUploadParser,)
    queryset = Warranty.objects.all()
    serializer_class = WarrantyApplicationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        user_profile_data, created = UserProfile.objects.get_or_create(user=user)
        if serializer.validated_data:
            user_profile_data.phone = request.POST.get('phone')
            user_profile_data.user.email = request.POST.get('email')
            user_profile_data.address = request.POST.get('address')
            user_profile_data.zipcode = request.POST.get('zipcode')
            user_profile_data.city = City.objects.get(id=request.POST.get('city'))
            user_profile_data.state = State.objects.get(code=request.POST.get('state'))
            user_profile_data.country = Country.objects.get(code=request.POST.get('country'))
            user_profile_data.user.save()
            user_profile_data.save()
            serializer.save(user_profile=user_profile_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChoicesListViewSet(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        country_list = [{'code': key, 'label': value} for key, value in OrderedDict(COUNTRIES).items()]
        company_choices = [{'code': key, 'label': value}for key, value in OrderedDict(COMPANY_CHOICES).items()]
        product_type = ProductType.objects.values('id', 'type_name')
        user_profile_countries = Country.objects.values('name', 'code')
        user_profile_state = State.objects.values('name', 'code')
        user_profile_city = City.objects.all()[:20].values('id', 'name')
        choice_dict = {'countries': country_list, 'companies': company_choices, 'product_type': product_type,
                       'user_profile_countries': user_profile_countries, 'user_profile_state': user_profile_state,
                       'user_profile_city': user_profile_city}
        return Response(choice_dict, 200)


class UserProfileView(ModelViewSet):

    http_method_names = ['get', 'PUT']

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(email=user_profile_data)

