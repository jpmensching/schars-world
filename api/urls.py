from django.conf.urls import patterns, url

from api import views

urlpatterns = patterns('',
	url(r'^categories/(?P<slug>[A-Za-z_\']+)/$', views.category, name='category'),
	url(r'^categories/$', views.categories, name='categories'),
	url(r'^articles/(?P<id>[0-9]+)/$', views.article ,name='categories'),
	url(r'^search/(?P<term>[A-Za-z_\']+)/(?P<batch>[0-9]+)/$', views.search, name='search')
)
