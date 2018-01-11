from django.db import models
from django_countries.fields import CountryField
from common.models import UserProfile
from product.models import ProductType

GENDER_CHOICES = (
    ('--', '--'),
    ('LG', 'LG'),
    ('APPLE', 'APPLE'),
    ('Samsung', 'Samsung'),
    ('HTC', 'HTC'),
)


class Warranty(models.Model):
    user_profile = models.ForeignKey(UserProfile, null=True)
    product = models.ForeignKey(ProductType)
    company_name = models.CharField(max_length=200, choices=GENDER_CHOICES, default=1)
    product_name = models.CharField(max_length=200, null=True, blank=True)
    product_color = models.CharField(max_length=200, null=True, blank=True)
    product_serial_no = models.CharField(max_length=30, null=True, blank=True)
    purchase_country = CountryField()
    purchase_date = models.DateField(auto_now_add=True)
    additional_info = models.CharField(max_length=200, null=True, blank=True)
    warranty_image = models.ImageField(upload_to='warranty_images/')

    def __str__(self):
        return self.user_profile


