from ..common import *  # noqa: ignore=F405

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio',
        'USER': 'portfolio',
        'PASSWORD': 'portfolio',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

CACHES['default']['LOCATION'] = os.environ.get('MEMCACHED_LOCATION', '127.0.0.1:11211') # noqa: ignore=F405
