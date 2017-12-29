from django import views
from django.conf.urls import url, include

from backend.innstal.common.views import UserCreate

urlpatterns = [
    url(r'api/register$', UserCreate.as_view(), name='account-create'),
]