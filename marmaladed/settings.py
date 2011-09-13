import os

#custom variables

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

PROJECT_NAME = 'Marmaladed'

MD_SERVERS = {
    'Virtual': {
        'LOCATION' : '127.0.0.1',
		'PORT' : '11211'
    },
    'Gvnn': {
        'LOCATION' : '10.3.55.141',
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