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


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id','product_name','user','product_category','product_type','product_brand',
                  'product_model','warranty_duration','installation_instruction',
                  'product_image1','product_manual','product_search_string','product_serial_number','manual_view_count')


    def update(self, instance, validated_data):
        manual_view_count = validated_data.pop('manual_view_count')
        instance.manual_view_count = manual_view_count
        instance.save()
        return instance


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ('id','name','category_image')