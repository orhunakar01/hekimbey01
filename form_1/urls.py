from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^download/(?P<pk>\d+)$', views.download, name='download'),
    url(r'^update/(?P<pk>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='delete'),
    url(r'^detail/(?P<pk>\d+)$', views.form1_detail, name='form1_detail'),
    url('create/', views.create, name='create'),
    url('', views.form1_view, name='form1_view'),

]

# urlpatterns+=staticfiles_urlpatterns()
# urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
