from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet, UpdateProductViewCount, ProductCategoryViewSet
from .views import SearchProductManual


router = DefaultRouter()
router.register(r'', ProductViewSet, base_name='products')
router.register(r'category/list', ProductCategoryViewSet, base_name='product_category')

urlpatterns = router.urls

urlpatterns = [
    url(r'update-viewcount/(?P<pk>\d+)/?$', UpdateProductViewCount.as_view()),
    url(r'search/$', SearchProductManual.as_view(), name='search'),
	# url(r'categories/$', ViewProductCategories.as_view(), name='categories'),
	url(r'^', include(router.urls)),
]