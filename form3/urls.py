from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^update/(?P<pk>\d+)$', views.update, name='update3'),
    url(r'^download/(?P<pk>\d+)$', views.download, name='download3'),
    url(r'^detail/(?P<pk>\d+)$', views.detail, name='detail3'),
    url(r'^delete/(?P<pk>\d+)$', views.delete , name='delete3'),
    url(r'^create/(?P<form1>\d+)$', views.create , name='create3') ,
    url(r'^malzeme/create/(?P<form3>\d+)$' , views.create_malzeme , name='create_malzeme'),
    url(r'^form3/id/malzeme/(?P<form3>\d+)$' , views.malzeme , name='views_malzeme'),
    url('', views.form3_view , name='form3_view'),
    ]