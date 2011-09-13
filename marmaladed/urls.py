from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns(
	'',
	url(r'^$', 'marmaladed.views.home', name='home'),
	url(r'^about$', 'marmaladed.views.about', name='about'),
	url(r'^console$', 'marmaladed.views.console', name='console'),
	url(r'^console/command$', 'marmaladed.console.command', name='command'),
	url(r'^server/([a-zA-Z0-9]+)/stats/$', 'marmaladed.views.stats', name='stats'),
	url(r'^server/([a-zA-Z0-9]+)/keys/$', 'marmaladed.views.keys', name='keys'),
	url(r'^gui/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT})
)