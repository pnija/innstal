from django.contrib import admin
from django.core.exceptions import PermissionDenied
import csv
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from common.models import *

admin.site.register(UserProfile)
admin.site.register(Blog)
admin.site.register(Newsletter)
admin.site.register(PricingPlan)

class AddCity(resources.ModelResource):
    class Meta:
        model = City


class ImportExportCountry(ImportExportModelAdmin):
    resource_class = AddCity
admin.site.register(City,ImportExportModelAdmin)


class AddCountry(resources.ModelResource):
    class Meta:
        model = Country


class ImportExportCountry(ImportExportModelAdmin):
    resource_class = AddCountry

admin.site.register(Country, ImportExportCountry)


class AddState(resources.ModelResource):
    class Meta:
        model = State
        exclude = ('country',)


class ImportExportAddState(ImportExportModelAdmin):
    resource_class = AddState
admin.site.register(State, ImportExportAddState)
