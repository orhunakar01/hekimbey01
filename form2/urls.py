from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^update/(?P<pk>\d+)$' , views.update , name='update2') ,
    url(r'^delete/(?P<pk>\d+)$' , views.delete , name='delete2') ,
    url(r'^detail/(?P<pk>\d+)$' , views.detail , name='detail2') ,
    url('create/(?P<form1>\d+)$' , views.create_view , name='create2') ,
    url('' , views.form2_view , name='form2_view') ,

]
