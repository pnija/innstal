from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from django.views.generic import TemplateView

from common.views import UserCreate, Logout, SubcribeNewsLetter, \
    UpdateNewsLetterSubscription, UpdatePassword, Login, BlogListingViewSet

router = routers.DefaultRouter()
router.register(r'blog', BlogListingViewSet)

urlpatterns = [
    url(r'^register/$', UserCreate.as_view(), name='account-create'),
    url(r'^login/$', Login.as_view()),
    url(r'^logout/$', Logout.as_view()),
    url(r'^reset-password/$', UpdatePassword.as_view()),
    url(r'^subcribe/newsletter/$', SubcribeNewsLetter.as_view()),
    url(r'^update/newsletter-subscription/$', UpdateNewsLetterSubscription.as_view(), name='subscribe'),
    url(r'^dashboard/$', TemplateView.as_view(template_name='views/dashboard.html'), name='dashboard'),
    url(r'^', include(router.urls)),
]
