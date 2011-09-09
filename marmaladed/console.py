#! /usr/bin/env python
from django.conf import settings
from django.http import HttpResponse
import memcache

def command(request):
	m = memcache.Memcache()
	#r = m.command("set key 0 900 4\n test")
	m.client.write("set key 0 900 4\r\n")
	m.client.write("test\r\n")
	r = m.client.read_until('STORED')
	m.close()
	return HttpResponse(r)