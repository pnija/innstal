from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProductManualSearchSerializer, ProductCategorySerializer
from .models import Product, ProductCategory


class SearchProductManual(generics.ListAPIView):
    serializer_class = ProductManualSearchSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search', None)

        if search:
            
            if self.request.user.is_authenticated():
                product = Product.objects.filter(product_search_string__icontains=search)
            else:
                product = Product.objects.filter(product_search_string__icontains=search)[:3]

            return product

        return Product.objects.none()


class ViewProductCategories(generics.ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset =  ProductCategory.objects.all()

