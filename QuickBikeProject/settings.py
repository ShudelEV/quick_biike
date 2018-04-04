"""
Django settings for QuickBikeProject project.

Generated by 'django-admin startproject' using Django 1.11.4.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '77epj25ja4piv8zvl6=nxi2abr53%q2jv3h6e4^&&#r()j2!l9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'webpack_loader',

    'django_extensions',

    'rest_framework',
    'Profile',
    'RentBike.apps.RentBikeConfig',
]

# Set our AUTH_USER_MODEL to a custom User model.
# Doing this will give us the same functionality but allow us to easily customize our User model
AUTH_USER_MODEL = 'Profile.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'QuickBikeProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'QuickBikeProject.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'quickbike_db',
        'USER': 'quickbike_user',
        'PASSWORD': 'velik5000',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# REST API to only be accessible to admin users

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 100
}

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
# STATIC_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

# Media static files (Images, Video)

MEDIA_ROOT = os.path.join(BASE_DIR, 'VueProject/public/')
MEDIA_URL = '/media/'


WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}
