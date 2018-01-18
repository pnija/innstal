from django_filters.rest_framework import FilterSet

from warranty.models import ClaimedWarranty


class ClaimFilter(FilterSet):
    class Meta:
        model = ClaimedWarranty
        fields = {
            'status'
        }
