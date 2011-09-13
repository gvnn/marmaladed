#! /usr/bin/env python
from django.conf import settings
from django.shortcuts import render_to_response
import memcache

def home(request):
	#load the stats of every server
	stats = {}
	for key, value in settings.MD_SERVERS.items():
		m = memcache.Memcache(value['LOCATION'], value['PORT'])
		m.outputmode = memcache.MemcacheOutput.VALUE
		stats[key] = m.stats()
	#render the template
	return render_to_response('bootstrap/home.html', {'settings': settings, 'module_home' : True, 'stats' : stats})
	
def about(request):
	return render_to_response('bootstrap/about.html', {'settings': settings, 'module_about' : True})
	
def console(request):
	return render_to_response('bootstrap/console.html', {'settings': settings, 'module_console' : True})