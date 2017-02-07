from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^signup/$', views.signup),
    # url(r'^$', views.home),
    # url(r'^$', views.login),
    url(r'^auth/$', views.auth_view),
    url(r'^after_login/$', views.after_login),
    url(r'^logout/$', views.logout),
]
