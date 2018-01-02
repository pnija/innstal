from django import views
from django.conf.urls import url, include

from common.views import UserCreate, login

urlpatterns = [
    url(r'api/register$', UserCreate.as_view(), name='account-create'),
    url(r'^login', login)
]