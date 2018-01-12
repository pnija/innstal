from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from django.views.generic import TemplateView

from common.views import UserCreate, Logout, SubcribeNewsLetter, \
    UpdateNewsLetterSubscription, UpdatePassword, Login, BlogListingViewSet,\
    ContactView, UpdateUserProfile, ActivateUserAccount, ForgotPassword,\
    ChangePassword, ResetPasswordCheck, GetUserProfile

router = routers.DefaultRouter()
router.register(r'blog', BlogListingViewSet)

urlpatterns = [
    url(r'^register/$', UserCreate.as_view(), name='account-create'),
    url(r'^login/$', Login.as_view()),
    url(r'^logout/$', Logout.as_view()),
    url(r'^account/activate/(?P<pk>\d+)/$', ActivateUserAccount.as_view()),
    url(r'^update/(?P<pk>\d+)/?$', UpdateUserProfile.as_view()),
    url(r'^forgot-password/', ForgotPassword.as_view()),
    url(r'^token-check/(?P<pk>\d+)?/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', ResetPasswordCheck.as_view()),
    url(r'^update-password/(?P<pk>\d+)?/$', ChangePassword.as_view()),
    url(r'^reset-password/$', UpdatePassword.as_view()),
    url(r'^subcribe/newsletter/$', SubcribeNewsLetter.as_view()),
    url(r'^update/newsletter-subscription/$', UpdateNewsLetterSubscription.as_view(), name='subscribe'),
    url(r'contact/$', ContactView.as_view(), name='contact'),
    url(r'profile/$', GetUserProfile.as_view(), name='profile'),
    url(r'^', include(router.urls)),
]
