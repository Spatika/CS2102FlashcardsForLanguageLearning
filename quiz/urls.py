from django.conf.urls import patterns, url
from quiz import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^set/create/', views.set_create, name='set_create'),
)