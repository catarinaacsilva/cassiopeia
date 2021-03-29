"""cassiopeia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^int/receipt', views.receiptManagement, name='receiptManagement'),
    url(r'^int/registerUser', views.formRegisterUser, name='formRegisterUser'),
    url(r'^register_user', views.registerUser, name='registerUser'),
    url(r'^addPolicy', views.addPolicy, name='addPolicy'),
    #url(r'^choosePolicy/', views.choosePolicy, name='choosePolicy'), 
    url(r'^giveConsent', views.giveConsent, name='giveConsent'),
    url(r'^addDevices', views.addDevices, name='addDevices'),    
]
