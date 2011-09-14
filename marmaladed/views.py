#! /usr/bin/env python
from django.core.context_processors import csrf
from django.conf import settings
from django.shortcuts import render_to_response
import unicodedata
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

def stats(request, server):
	server_settings = settings.MD_SERVERS[server]
	m = memcache.Memcache(server_settings['LOCATION'], server_settings['PORT'])
	m.outputmode = memcache.MemcacheOutput.VALUE
	complete_stats = m.stats()
	return render_to_response('bootstrap/stats.html', {'settings': settings, 'stats' : complete_stats, 'server' : server_settings})

def console(request):
	return render_to_response('bootstrap/console.html', {'settings': settings, 'module_console' : True})
	
def key(request, server):
	#get server details
	server_settings = settings.MD_SERVERS[server]
	#try get key
	key_dict = {}
	key_name = ""
	if request.method == 'POST':
		key_name = unicodedata.normalize('NFKD', request.POST["key_name"]).encode('ascii','ignore')
		m = memcache.Memcache(server_settings['LOCATION'], server_settings['PORT'])
		m.outputmode = memcache.MemcacheOutput.VALUE
		key_dict = m.get(key_name)
	return render_to_response('bootstrap/key.html', {'settings': settings, 'server' : server_settings, 'key' : key_dict, 'key_name' : key_name, 'server_label' : server})