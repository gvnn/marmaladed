import os

#custom variables

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

PROJECT_NAME = 'Marmaladed'

PROJECT_VERSION = '0.3'

MD_SERVERS = {
    'local': {
		'DESCRIPTION' : 'Local Machine',
        'LOCATION' : '127.0.0.1',
		'PORT' : '11211'
	}
}

#django variables

DEBUG = True

TEMPLATE_DEBUG = DEBUG

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/'
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.middleware.csrf.CsrfResponseMiddleware',
)

STATIC_DOC_ROOT = PROJECT_PATH + '/static/'

ROOT_URLCONF = 'marmaladed.urls'

INSTALLED_APPS = ('marmaladed') 