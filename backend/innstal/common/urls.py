
from django import views
from django.conf.urls import url, include
from django.conf.urls import url
from django.contrib import admin
from common.views import UserCreate, Logout, login

urlpatterns = [
    url(r'api/register$', UserCreate.as_view(), name='account-create'),
    url(r'^login', login),
    url(r'^logout/', Logout.as_view()),
]



