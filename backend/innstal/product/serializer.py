from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id','product_name','user','product_category','product_type','product_brand',
                  'product_model','warranty_duration','installation_instruction',
                  'product_image1','product_manual','product_search_string','product_serial_number','manual_view_count')


    def update(self, instance, validated_data):
        # instance.manual_view_count = validated_data.get('manual_view_count', instance.manual_view_count)
        manual_view_count = validated_data.pop('manual_view_count')
        instance.manual_view_count = manual_view_count
        instance.save()
        return instance