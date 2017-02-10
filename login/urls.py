from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^signup/$', views.signup),
    # url(r'^$', views.home),
    # url(r'^$', views.login),

    url(r'^auth/$', views.auth_view),
    url(r'^after_login/$', views.after_login),
    url(r'^logout/$', views.logout),
    url(r'^Ist_Year/$', views.Iyear),
    url(r'^IInd_Year/$', views.IIyear),
    url(r'^IIIrd_Year/$', views.IIIyear),
    url(r'^IVth_Year/$', views.IVyear),
    url(r'^upload/', include('upload_data.urls')),
]
