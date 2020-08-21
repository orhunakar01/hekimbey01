from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^update/(?P<pk>\d+)$', views.form6_update, name='update6'),
    url(r'^delete/(?P<pk>\d+)$', views.form6_delete, name='delete6'),
    url(r'^create/', views.form6_create , name='create6') ,
    url('', views.form6_firmalar, name='Firmalar6'),



        ]
