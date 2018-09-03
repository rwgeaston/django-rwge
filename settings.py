SECRET_KEY = 'only for tests'

import os

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
