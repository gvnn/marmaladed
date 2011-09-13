import os

#custom variables

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

PROJECT_NAME = 'Marmaladed'

MD_SERVERS = {
    'virtual': {
		'DESCRIPTION' : 'Virtual machine',
        'LOCATION' : '127.0.0.1',
		'PORT' : '11211'
    },
    'gvnn': {
        'DESCRIPTION' : 'Gvnn\'s server',
        'LOCATION' : '10.0.22.10',
		'PORT' : '11211'
    }
}

#django variables

DEBUG = True

TEMPLATE_DEBUG = DEBUG

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/'
)

STATIC_DOC_ROOT = PROJECT_PATH + '/static/'

ROOT_URLCONF = 'marmaladed.urls'

INSTALLED_APPS = ('marmaladed') 