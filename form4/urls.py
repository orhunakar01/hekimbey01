from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^update/(?P<pk>\d+)$', views.update, name='update4'),
    url(r'^delete/(?P<pk>\d+)$', views.delete , name='delete4'),
    url(r'^create/(?P<form1>\d+)$', views.create , name='create4') ,
    url(r'^detail/(?P<pk>\d+)$' , views.detail , name='detail4') ,

    url('', views.form4_view , name='form4_view'),
    ]

