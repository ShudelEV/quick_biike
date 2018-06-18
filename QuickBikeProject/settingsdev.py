from .settings import *

DEBUG = True
INTERNAL_IPS = ['127.0.0.1']
ALLOWED_HOSTS += INTERNAL_IPS
ALLOWED_HOSTS.append('localhost')

INSTALLED_APPS.append('silk')
MIDDLEWARE.append('silk.middleware.SilkyMiddleware',)
# SILKY_PYTHON_PROFILER = True
