from django.db import models
from common.models import *
from product.models import *


class Warranty(models.Model):
    product = models.ForeignKey(Product)
    user = models.ForeignKey(UserProfile)
    warranty_image = models.ImageField(upload_to='warranty_images/')


    def __str__(self):
        return self.product.product_name

