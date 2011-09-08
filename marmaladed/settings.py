import os

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DEBUG = True

TEMPLATE_DEBUG = DEBUG

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/'
)

STATIC_DOC_ROOT = PROJECT_PATH + '/static/'

ROOT_URLCONF = 'marmaladed.urls'