from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet, UpdateProductViewCount, ProductCategoryViewSet
from .views import SearchProductManual, ViewProductCategories


router = DefaultRouter()
router.register(r'', ProductViewSet, base_name='products')
router.register(r'(?P<id>\d+)/?$', ProductViewSet, base_name='products')
router.register(r'category/list', ProductCategoryViewSet, base_name='product_category')
router.register(r'category/(?P<id>\d+)/?$', ProductCategoryViewSet, base_name='product_category')
urlpatterns = router.urls

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'update-viewcount/(?P<pk>\d+)/?$', UpdateProductViewCount.as_view()),
    url(r'search/$', SearchProductManual.as_view(), name='search'),
	url(r'categories/$', ViewProductCategories.as_view(), name='categories'),
]