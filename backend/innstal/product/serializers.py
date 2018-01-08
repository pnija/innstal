from rest_framework import serializers

from .models import Product, ProductCategory


class ProductManualSearchSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		fields = ('id', 'product_name', 'product_category', 'product_type', 'product_brand',
		'product_model', 'warranty_duration', 'installation_instruction', 'product_image1', 'product_manual')
		depth = 1

class ProductCategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductCategory
		fields = ('id','name','category_image')