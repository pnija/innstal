from rest_framework.viewsets import ModelViewSet
from .models import Warranty
from .serializers import WarrantyApplicationSerializer
# Create your views here.


class WarrantApplicationViewSet(ModelViewSet):
    queryset = Warranty.objects.all()
    serializer_class = WarrantyApplicationSerializer
