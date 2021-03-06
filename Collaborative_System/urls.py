"""Collaborative_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import home
from rest_framework.urlpatterns import format_suffix_patterns
from login import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('login.urls')),
    # url(r'^upload_data/', include('upload_data.urls')),
    url(r'^$', home),
    url(r'^Sign_Up_Data/', views.Sign_Up_DataList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)