"""
Django settings for samplesite project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))
MEDIA_DIR = os.path.join(BASE_DIR, 'media/images')
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

THUMBNAIL_ALIASES = {
    '': {
        'default': {
            'size': (90, 90),
            'crop': 'scale',
        },
    },
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3sy5v88nn@7-v23q^m_7i4+n*dx+4=8c_h=y6gewu%5zc7jj8!'

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.postgres',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'board.apps.BoardConfig',
    'accounts.apps.AccountsConfig',
    'django_cleanup',
    'easy_thumbnails',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'samplesite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'samplesite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
AUTH_PWD_MODULE = 'django.contrib.auth.password_validation.'

AUTH_PASSWORD_VALIDATORS = [
    {
        f'NAME': f'{AUTH_PWD_MODULE}UserAttributeSimilarityValidator',
    },
    {
        'NAME': f'{AUTH_PWD_MODULE}MinimumLengthValidator',
    },
    {
        'NAME': f'{AUTH_PWD_MODULE}CommonPasswordValidator',
    },
    {
        'NAME': f'{AUTH_PWD_MODULE}NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

SHORT_DATETIME_FORМAT = 'd.m.Y h:i'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'alexgoryachev2904@gmail.com'
EMAIL_HOST_PASSWORD = 'Alex33456645'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

GOOGLE_RECAPTCHA_SECRET_KEY = '6LdR40kaAAAAAPDwLcb4Lg-mQkbLa2AbX6x03PCU'

CORS_ORIGIN_ALLOW_ALL=True
CORS_URLS_REGEX = r'^/api/.*$'

