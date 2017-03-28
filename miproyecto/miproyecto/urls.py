from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms import views

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.lista_paginas),
    url(r'(.+)/(.+)', views.nuevonombre),
    url(r'(.+)', views.pages),
    url(r'(.*)/(.*)', views.mi404),
)
