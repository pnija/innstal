from django.conf.urls import url, include
from warranty.views import WarrantApplicationViewSet, UserProfileView,ChoicesListViewSet
from rest_framework import routers


router = routers.DefaultRouter()
# router.register(r'country-list', CountryListViewSet, base_name='countries')
router.register(r'register', WarrantApplicationViewSet, base_name='register')
router.register(r'users', UserProfileView, base_name='users')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'country-list', ChoicesListViewSet.as_view(), name='countries'),

]

