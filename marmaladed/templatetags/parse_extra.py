#! /usr/bin/env python
from django import template
import time

register = template.Library()

@register.filter(name='duration')
def duration(secs):
	years = int(((secs/(7*86400))/52.177457))
	#rem = int(((secs-(years * 52.177457 * 7 * 86400))))
    #weeks = int(((rem)/(7*86400)))
    #days = int(((rem)/86400) - weeks*7)
    #hours = int(((rem)/3600) - days*24 - weeks*7*24)
    #mins = int(((rem)/60) - hours*60 - days*24*60 - weeks*7*24*60)
	returnstring = ""
	#if($years==1) $str .= "$years year, ";
    #if($years>1) $str .= "$years years, ";
    #if($weeks==1) $str .= "$weeks week, ";
    #if($weeks>1) $str .= "$weeks weeks, ";
    #if($days==1) $str .= "$days day,";
    #if($days>1) $str .= "$days days,";
    #if($hours == 1) $str .= " $hours hour and";
    #if($hours>1) $str .= " $hours hours and";
    #if($mins == 1) $str .= " 1 minute";
    #else $str .= " $mins minutes";
    #return returnstring
	return returnstring