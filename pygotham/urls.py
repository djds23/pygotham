from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'transcoder.views.index', name='index'),
    url(r'^transcoder/url', 'transcoder.views.twitter_handler', name='handler'),
    url(r'^admin/', include(admin.site.urls))
)
