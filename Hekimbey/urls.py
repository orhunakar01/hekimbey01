"""Hekimbey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('form1/' , include('form_1.urls')) ,
    url('form2/' , include('form2.urls')) ,
    url('form3/' , include('form3.urls')) ,
    url('form4/' , include('form4.urls')) ,
    url('form5/' , include('form5.urls')) ,
    url('anasayfa/' , include('anasayfa.urls')) ,
    url('form6/' , include('Firmalar.urls')) ,
    url('', include('giris.urls')),




]
