"""moversandpackersmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from mpmanagement.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('admin_login', admin_login, name='admin_login'),
    path('admin_home', admin_home, name='admin_home'),
    path('logout', Logout, name='logout'),
    path('add_services', add_services, name='add_services'),
    path('manage_services', manage_services, name='manage_services'),
    path('edit_service/<int:pid>', edit_service, name='edit_service'),
    path('delete_service/<int:pid>', delete_service, name='delete_service'),
    path('services', services, name='services'),
    path('about', about, name='about'),          
    path('request_form', request_form, name="request_form"),
    path('new_booking', new_booking, name="new_booking"),
    path('old_booking', old_booking, name="old_booking"),
    path('view_bookingdetail/<int:pid>', view_bookingdetail, name="view_bookingdetail"),
    path('delete_booking/<int:pid>', delete_booking, name='delete_booking'),
    path('contact', contact, name='contact'),
    path('new_messages', new_messages, name="new_messages"),
    path('old_messages', old_messages, name="old_messages"),
    path('view_messagesdetail/<int:pid>', view_messagesdetail, name="view_messagesdetail"),
    path('delete_message/<int:pid>', delete_message, name='delete_message'),
    path('search', search, name='search'),     
    path('bookingreport_betweendates', bookingreport_betweendates, name='bookingreport_betweendates'),   
    path('msgsform_betweendates', msgsform_betweendates, name='msgsform_betweendates'),  
    path('change_password', change_password, name='change_password'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
