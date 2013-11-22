from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from ops.views import *

urlpatterns = patterns('',
    url(r'^$', home_page, name="home_page"),
    url(r'^papers/', papers_page, name="papers_page"),
    url(r'^about/', about_page, name="about_page"),
    url(r'^contrib/', contrib_page, name="contrib_page"),
    url(r'^admin/', include(admin.site.urls)),
)
