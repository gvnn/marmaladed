#! /usr/bin/env python
from django.conf import settings
from django.shortcuts import render_to_response

def home(request):
	return render_to_response('bootstrap/home.html', {'settings': settings, 'module_home' : True})
	
def about(request):
	return render_to_response('bootstrap/about.html', {'settings': settings, 'module_about' : True})
	
def console(request):
	return render_to_response('bootstrap/console.html', {'settings': settings, 'module_console' : True})