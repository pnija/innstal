from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from .serializers import ProductManualSearchSerializer, ProductCategorySerializer, ProductSerializer
from .models import Product, ProductCategory


class SearchProductManual(generics.ListAPIView):
    serializer_class = ProductManualSearchSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search', None)
        if search:
            if self.request.user.is_authenticated():

                products = Product.objects.filter(product_search_string__icontains=search).order_by('product_name')

            else:
                products = Product.objects.filter(product_search_string__icontains=search).order_by('product_name')[:3]

            return products

        return Product.objects.none()


# class ViewProductCategories(generics.ListAPIView):
#     serializer_class = ProductCategorySerializer
#     queryset =  ProductCategory.objects.all()


class ProductViewSet(ViewSet):
    def list(self, request):
        response = {}
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        response['status'] = 'success'
        response['message'] = 'Products listed successfully'
        response['products'] = serializer.data
        return Response(response)

    def retrieve(self, request, pk=None):
        response = {}
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        response['status'] = 'success'
        response['message'] = 'Product detail fetched successfully'
        response['product_detail'] = serializer.data
        return Response(serializer.data)

    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.serialize(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class UpdateProductViewCount(APIView):
    def get(self, request, pk):
        response = {}
        request_data = Product.objects.filter(pk=pk)
        if request_data:
            request_data = Product.objects.get(pk=pk)
            manual_view_count = request_data.manual_view_count
            manual_view_count = manual_view_count + 1
            request_data.manual_view_count = manual_view_count
            Product.objects.filter(pk=pk).update(manual_view_count=manual_view_count)
            response['status'] = 'success'
            response['message'] = 'manual view count updated'
            return Response(response, status=status.HTTP_200_OK)
        else:
            response['status'] = 'failed'
            response['message'] = 'Product Does not exist'
            return Response(response)

class ProductCategoryViewSet(ViewSet):
    def list(self, request):
        response = {}
        queryset = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(queryset, many=True)
        response['status'] = 'success'
        response['message'] = 'Products listed successfully'
        response['products'] = serializer.data
        return Response(response)

    def retrieve(self, request, pk=None):
        response = {}
        queryset = ProductCategory.objects.all()
        product_category = get_object_or_404(queryset, pk=pk)
        serializer = ProductCategorySerializer(product_category)
        response['status'] = 'success'
        response['message'] = 'Product detail fetched successfully'
        response['product_detail'] = serializer.data
        return Response(serializer.data)
