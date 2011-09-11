#! /usr/bin/env python
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import unicodedata
import memcache

@csrf_exempt
def command(request):
	if request.POST["command"]:
		command = request.POST["command"]
		args = ""
		value = ""
		
		if "args" in request.POST:
			args = unicodedata.normalize('NFKD', request.POST["args"]).encode('ascii','ignore')
		
		if "value" in request.POST:
			value = unicodedata.normalize('NFKD', request.POST["value"]).encode('ascii','ignore')
			
		switch = {
			'stats': lambda m: m.stats(args),
			'get': lambda m: m.get(args),
			'delete': lambda m: m.delete(args),
			'add': lambda m: m.storage("add", args, value),
			'set': lambda m: m.storage("set", args, value),
			'replace': lambda m: m.storage("replace", args, value),
			'append': lambda m: m.storage("append", args, value),
			'prepend': lambda m: m.storage("prepend", args, value),
			'cas': lambda m: m.storage("cas", args, value)
		}
		if command in switch:
			m = memcache.Memcache()
			m.outputmode = memcache.MemcacheOutput.CONSOLE
			r = switch[command](m)
			return HttpResponse(r)
		else:
			return HttpResponseBadRequest()
	else:
		return HttpResponseBadRequest()