#! /usr/bin/env python
from django import template

register = template.Library()

@register.filter(name='getkey')
def getkey(value, arg):
	if arg in value:
		return value[arg]
	else:
		return ""