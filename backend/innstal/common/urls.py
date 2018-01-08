from django.conf.urls import url

from common.views import UserCreate, Logout, SubcribeNewsLetter, \
    UpdateNewsLetterSubscription, UpdatePassword, Login

urlpatterns = [
    url(r'^register$', UserCreate.as_view(), name='account-create'),
    url(r'^login', Login.as_view()),
    url(r'^logout/', Logout.as_view()),
    url(r'^reset-password/', UpdatePassword.as_view()),
    url(r'^subcribe/newsletter', SubcribeNewsLetter.as_view()),
    url(r'^update/newsletter-subscription', UpdateNewsLetterSubscription.as_view(), name='subscribe'),
]

