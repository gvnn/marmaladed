![marmaladed](https://github.com/gvnn/marmaladed/raw/master/resources/logo.md.png)

a simple django memcached console

**Getting Started**

* install python-memcached

	http://www.tummy.com/Community/software/python-memcached/
	
	or
	
	http://sendapatch.se/projects/pylibmc/
	

* Add marmaladed to your INSTALLED_APPS setting:

	INSTALLED_APPS = (
		# ...
		'marmaladed',
	)
	   
* Add the urls to your url configuration::

	urlpatterns = patterns('',
		# ...
		(r'^marmaladed/', include('marmaladed.urls')),
	)