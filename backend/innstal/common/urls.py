
from django import views
from django.conf.urls import url, include
from django.conf.urls import url
from django.contrib import admin
from common.views import UserCreate, Logout, SubcribeNewsLetter, UpdateNewsLetterSubscription,\
 Login, ContactView


urlpatterns = [
    url(r'^user/register$', UserCreate.as_view(), name='account-create'),
    url(r'^user/login', Login.as_view()),
    url(r'^user/logout/', Logout.as_view()),
    url(r'^user/subcribe/', SubcribeNewsLetter.as_view()),
    url(r'^user/update/subscription', UpdateNewsLetterSubscription.as_view(), name='subscribe'),
    url(r'contact/$', ContactView.as_view(), name='contact'),
]
