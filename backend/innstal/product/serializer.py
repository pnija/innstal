from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('product_name','user','product_category','product_type','product_brand',
                  'product_model','warranty_duration','installation_instruction',
                  'product_image1','product_manual','product_search_string','product_serial_number','manual_view_count')

