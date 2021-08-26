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
    url(r'^int/registerUser', views.formRegisterUser, name='formRegisterUser'),
    url(r'^int/registerStay', views.formRegisterStay, name='formRegisterStay'),
    url(r'^int/addPolicy', views.formAddPolicy, name='formAddPolicy'),
    url(r'^int/addDevice', views.formAddDevice, name='formAddDevice'),
    url(r'^int/addEntity', views.formAddEntity, name='formAddEntity'),
    url(r'^int/listPolices', views.listPolicies, name='listPolicies'),
    url(r'^int/listDevices', views.listDevices, name='listDevices'),
    url(r'^int/listEntities', views.listEntities, name='listEntities'),
    url(r'^int/listUsers', views.listUsers, name='listUsers'),
    url(r'^int/listReceipts', views.listReceipts, name='listReceipts'),
    url(r'^int/listSReceipts', views.listSReceipts, name='listSReceipts'),
    url(r'^int/notifications', views.notifications, name='notifications'),
    
    url(r'^register_user', views.registerUser, name='registerUser'),
    url(r'^adddevice', views.addDevice, name='addDevice'),
    url(r'^addentity', views.addEntity, name='addEntity'),
    url(r'^addpolicy', views.addPolicy, name='addPolicy'),
    url(r'^adduser', views.registerUser, name='registerUser'),
    url(r'^addstay', views.registerStay, name='registerStay'), 
    url(r'^sign', views.signReceipt, name='signReceipt'),
    url(r'^requestDeletion', views.requestDeletion, name='requestDeletion'),
    url(r'^confirmDeletion', views.confirmDeletion, name='confirmDeletion'),
]
