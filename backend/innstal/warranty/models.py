from django.db import models
from django_countries.fields import CountryField
from common.models import UserProfile
from product.models import ProductType
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

COMPANY_CHOICES = (
    ('--', '--'),
    ('LG', 'LG'),
    ('APPLE', 'APPLE'),
    ('Samsung', 'Samsung'),
    ('HTC', 'HTC'),
)


class Warranty(models.Model):
    user_profile = models.ForeignKey(UserProfile, null=True, related_name='get_user_warranty')
    product = models.ForeignKey(ProductType)
    company_name = models.CharField(max_length=200, choices=COMPANY_CHOICES, default=1)
    product_name = models.CharField(max_length=200, null=True, blank=True)
    product_color = models.CharField(max_length=200, null=True, blank=True)
    product_serial_no = models.CharField(max_length=30, null=True, blank=True)
    purchase_country = CountryField()
    purchase_date = models.DateField(auto_now_add=True)
    additional_info = models.CharField(max_length=2000, null=True, blank=True)
    warranty_image = models.ImageField(upload_to='warranty_images/')

    def save(self, force_insert=False, force_update=False, using=None):

        im = Image.open(self.warranty_image)

        output = BytesIO()

        im = im.resize((215, 300))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.warranty_image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.warranty_image.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)

        super(Warranty, self).save()

    def __str__(self):
        return self.product.type_name


class ClaimedWarranty(models.Model):
    user = models.ForeignKey(UserProfile, null=True)
    warranty = models.ForeignKey(Warranty)
    is_active = models.BooleanField
    status = models.CharField(max_length=200)
    claimed_date = models.DateField(auto_now_add=True)



