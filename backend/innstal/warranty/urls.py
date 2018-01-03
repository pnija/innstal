from django.conf.urls import url, include
from warranty.views import WarrantApplicationViewSet, UserProfileView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'register', WarrantApplicationViewSet)
router.register(r'users', UserProfileView)

urlpatterns = [
    url(r'^', include(router.urls)),

]

