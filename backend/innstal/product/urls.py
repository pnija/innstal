from django.conf.urls import url
from django.contrib import admin

from .views import SearchProductManual


urlpatterns = [
	url(r'search/$', SearchProductManual.as_view(), name='search'),
]