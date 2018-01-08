from django.conf.urls import url
from django.contrib import admin

from .views import SearchProductManual, ViewProductCategories


urlpatterns = [
	url(r'search/$', SearchProductManual.as_view(), name='search'),
	url(r'categories/$', ViewProductCategories.as_view(), name='categories'),
]