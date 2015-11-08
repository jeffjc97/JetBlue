from django.conf.urls import patterns, include, url
from django.contrib import admin

from api import views

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^query/(?P<airports>(.*))/option/(?P<option>\d{1})/', views.query, name='query'),
	url(r'^details/(?P<id>\d*)/', views.details, name='details'),
)