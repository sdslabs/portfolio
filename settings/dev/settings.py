from ..common import *  # noqa: ignore=F405

DEBUG = True

CORS_ORIGIN_ALLOW_ALL = DEBUG
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio',
        'USER': 'ishu',
        'PASSWORD': 'Ishan_002',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

CACHES['default']['LOCATION'] = os.environ.get('MEMCACHED_LOCATION', 'db:11211') # noqa: ignore=F405
