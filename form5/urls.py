from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^update/(?P<pk>\d+)$', views.update, name='update5'),
    url(r'^download/(?P<pk>\d+)$', views.download, name='download5'),
    url(r'^detail/(?P<pk>\d+)$', views.detail, name='detail5'),
    url(r'^delete/(?P<pk>\d+)$', views.delete , name='delete5'),
    url(r'^create/(?P<form1>\d+)$', views.create , name='create5') ,
    url('', views.form5_view, name='form5_view'),
    ]