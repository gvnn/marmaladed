#! /usr/bin/env python
from django import template
import time

register = template.Library()

@register.filter(name='duration')
def duration(delta):
	secs = int(delta)
	years = int(((secs / (7*86400))/ 52.177457))
	rem = int(((secs-(years * 52.177457 * 7 * 86400))))
	weeks = int(((rem)/(7*86400)))
	days = int(((rem)/86400) - weeks*7)
	hours = int(((rem)/3600) - days*24 - weeks*7*24)
	mins = int(((rem)/60) - hours*60 - days*24*60 - weeks*7*24*60)
	returnstring = ""
	if years == 1 : returnstring += "1 year, "
	if years > 1 : returnstring += "%s years, " % years
	if weeks == 1 : returnstring += "%s week, " % weeks
	if weeks > 1 : returnstring += "%s weeks, " % weeks
	if days ==1 : returnstring += "%s day, " % days
	if days > 1 : returnstring += "%s days, " % days
	if hours == 1 : returnstring += " %s hour and" % hours
	if hours > 1 : returnstring += " %s hours and" % hours
	if mins == 1 : returnstring += " 1 minute";
	else: returnstring += " %s minutes" % mins
	return returnstring