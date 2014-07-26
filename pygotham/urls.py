from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'transcoder.views.index', name='index'),
    url(r'^transcoder/url', 'transcoder.views.yt_url_handler', name='handler'),
    url(r'^admin/', include(admin.site.urls))
)
