from django.contrib import admin
from .models import Warranty, ClaimedWarranty

# Register your models here.
admin.site.register(Warranty)
admin.site.register(ClaimedWarranty)
