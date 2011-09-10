#! /usr/bin/env python
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import unicodedata
import memcache

@csrf_exempt
def command(request):
	if request.POST["command"]:
		command = request.POST["command"]
		args = ""
		if "args" in request.POST:
			args = unicodedata.normalize('NFKD', request.POST["args"]).encode('ascii','ignore')
			
		switch = {
			'stats': lambda m: m.stats(args)
		}
		if command in switch:
			m = memcache.Memcache()
			r = switch[command](m)
			return HttpResponse(r)
		else:
			return HttpResponseBadRequest()
	else:
		return HttpResponseBadRequest()