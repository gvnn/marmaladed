from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^$', 'marmaladed.views.home', name='home'),
	url(r'^about$', 'marmaladed.views.about', name='about'),
	url(r'^console$', 'marmaladed.views.console', name='console'),
	url(r'^console/command$', 'marmaladed.console.command', name='command'),
	url(r'^gui/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT})
    # url(r'^marmaladed/', include('marmaladed.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)