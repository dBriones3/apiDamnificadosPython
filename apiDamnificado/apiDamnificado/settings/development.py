from .base import *

DEBUG = True
ALLOWED_HOST = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'damnificadosDB',
        'USER': 'root',
        'PASSWORD': 'Jessica1-',
        'HOST': 'docker-mysql-2',
        'PORT': ''
    }
}

REST_FRAMEWORK = {
   'DEFAULT_PERMISSION_CLASSES': (
       'rest_framework.permissions.AllowAny',
   ),
   'DEFAULT_AUTHENTICATION_CLASSES': (
       'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
       'rest_framework.authentication.SessionAuthentication',
       'rest_framework.authentication.BasicAuthentication',
   ),
}