from django.conf.urls import url, include
from warranty.views import WarrantApplicationViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'register', WarrantApplicationViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),

]

