import os
import sys

SECRET_KEY = 'only for tests'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.messages',

    'rwge',
]

ROOT_URLCONF = 'rwge.urls'

RWGE_URL = 'abc'
RWGE_SECRET = '123'
DEBUG = True

PEOPLE_TO_ASK = ['tom', 'dick', 'harry']

DEFAULT_MOTHER_FREQUENCY = 40

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'log_to_stdout': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        },
    },
    'loggers': {
        'rwge': {
            'handlers': ['log_to_stdout'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}