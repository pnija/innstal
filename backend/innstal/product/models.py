from django.db import models
from common.models import *
# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField('Product Category', max_length=50)
    category_image = models.ImageField(upload_to='category_directory_path/', blank=True, null=True)

    def __str__(self):
        return self.name

class ProductType(models.Model):
    type_name = models.CharField('Type Name', max_length=50)
    category = models.ForeignKey(ProductCategory, blank=True, null=True)

    def __str__(self):
        return self.type_name

class ProductBrand(models.Model):
    brand_name = models.CharField('Brand Name', max_length=50)

    def __str__(self):
        return self.brand_name

class Product(models.Model):
    product_name = models.CharField('Product Name', max_length=50)
    user = models.ForeignKey(UserProfile, blank=True, null=True)
    product_category = models.ForeignKey(ProductCategory, blank=True, null=True)
    product_type = models.ForeignKey(ProductType, blank=True, null=True)
    product_brand = models.ForeignKey(ProductBrand, blank=True, null=True)
    product_model = models.CharField('Model No', max_length=50, blank=True, null=True)
    warranty_duration = models.CharField('Warranty In Days', max_length=5, blank=True, null=True)
    installation_instruction = models.TextField(max_length=500, blank=True, null=True)
    product_image1 = models.ImageField(upload_to='product_image_path', blank=True, null=True)
    product_manual = models.FileField(upload_to='product_manual_path', blank=True, null=True)
    product_search_string = models.TextField(max_length=500, blank=True, null=True, editable=False)
    product_serial_number = models.CharField(max_length=20, blank=True, null=True)
    manual_view_count = models.IntegerField()

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):

        string = self.product_name + " "
        if self.product_model:
            string += self.product_model + " "

        if self.product_brand:
            string += self.product_brand.brand_name + " "

        if self.product_category:
            string += self.product_category.name + " "
        self.product_search_string = string
        super(Product, self).save(*args, **kwargs)


class ProductVisited(models.Model):
    product = models.ForeignKey(Product)
    visitor = models.ForeignKey(UserProfile)
    visite_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.product.product_name