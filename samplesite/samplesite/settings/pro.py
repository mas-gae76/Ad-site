from .base import *


DEBUG = True

ADMINS = (
    ('Alex G', 'alex2904.goryachev@yandex.com')
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'boards',
        'USER': 'postgres',
        'PASSWORD': 'mas8135',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}
