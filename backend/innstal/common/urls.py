from django.conf.urls import url
from django.views.generic import TemplateView

from common.views import UserCreate, Logout, SubcribeNewsLetter, \
    UpdateNewsLetterSubscription, UpdatePassword, Login, ActivateUserAccount, ForgotPassword, ResetPasswordCheck, \
    ChangePassword

urlpatterns = [
    url(r'^register/$', UserCreate.as_view(), name='account-create'),
    url(r'^login/$', Login.as_view()),
    url(r'^logout/$', Logout.as_view()),
    url(r'^account/activate/(?P<pk>\d+)/?$', ActivateUserAccount.as_view()),
    url(r'^forgot-password/', ForgotPassword.as_view()),
    url(r'^token-check/(?P<pk>\d+)?/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', ResetPasswordCheck.as_view()),
    url(r'^update-password/(?P<pk>\d+)?/$', ChangePassword.as_view()),
    url(r'^reset-password/$', UpdatePassword.as_view()),
    url(r'^subcribe/newsletter/$', SubcribeNewsLetter.as_view()),
    url(r'^update/newsletter-subscription/$', UpdateNewsLetterSubscription.as_view(), name='subscribe'),
    url(r'^dashboard/$', TemplateView.as_view(template_name='views/dashboard.html'), name='dashboard'),
]

