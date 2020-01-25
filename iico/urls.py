"""iico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.index2, name='index'),
    url(r'^signin/', views.login, name='post'),
    url(r'^account/', views.account, name='post'),
    url(r'^account2/', views.account2, name='post'),
    url(r'^form/', views.form, name='form'),
    url(r'^update/', views.update, name='form'),
    url(r'^upload/', views.upload, name='form'),
]

urlpatterns+=staticfiles_urlpatterns()


