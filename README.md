![marmaladed](https://github.com/gvnn/marmaladed/raw/master/resources/logo.md.png)

a simple django memcached console

**Getting Started**

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