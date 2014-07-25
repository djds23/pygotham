from django.conf.urls import patterns, include, url

from django.contrib import admin

from transcoder.views import home

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'transcoder.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
