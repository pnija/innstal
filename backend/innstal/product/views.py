from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from product.models import Product
from product.serializer import ProductSerializer



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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serialize(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)