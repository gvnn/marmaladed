#! /usr/bin/env python
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import memcache

@csrf_exempt
def command(request):
	if request.POST["command"]:
		command = request.POST["command"]
		switch = {
			'stats': lambda m: m.stats()
		}
		if command in switch:
			m = memcache.Memcache()
			r = switch[command](m)
			return HttpResponse(r)
		else:
			return HttpResponseBadRequest()
	else:
		return HttpResponseBadRequest()