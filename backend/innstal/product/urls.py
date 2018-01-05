from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet


router = DefaultRouter()
router.register(r'', ProductViewSet, base_name='products')
router.register(r'/(?P<id>\d+)/?$', ProductViewSet, base_name='products')
router.register(r'/(?P<id>\d+)/?update$', ProductViewSet, base_name='products')
urlpatterns = router.urls


urlpatterns = [
url(r'^', include(router.urls)),
]