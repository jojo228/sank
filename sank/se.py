import os
from typing import Any, Dict
from pathlib import Path
from django.conf.global_settings import LANGUAGES as DJANGO_LANGUAGES
from django.core.management.utils import get_random_secret_key
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = os.getenv('DEBUG', 'False') == 'False'

if not DEBUG:
    DEBUG_PROPAGATE_EXCEPTIONS = True

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1").split(',')
DEVELOPMENT_MODE = os.getenv('DEVELOPMENT_MODE', 'False') == 'True'

# ALLOWED_HOSTS = ['127.0.0.1', '192.168.1.80']

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sites',
    'django.contrib.humanize',
]

THIRD_PARTY_APPS = [
    "django_countries", "django_seed", "storages", "mathfilters"  
    ]


PROJECT_APPS = [
    
    "main.apps.MainConfig",
    "rooms.apps.RoomsConfig",
    "lists.apps.ListsConfig",
]


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.middleware.locale.LocaleMiddleware",

]

ROOT_URLCONF = 'sank.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'sank.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
# DATABASES = {
#             'default': {
#                 'ENGINE': os.getenv('DB_ENGINE'),
#                 'NAME': os.getenv('DB_NAME'),
#                 'USER': os.getenv('DB_USER'),
#                 'PASSWORD': os.getenv('DB_PASSWORD'),
#                 'HOST': os.getenv('DB_HOST'),
#                 'PORT': os.getenv('DB_PORT'),
#             }
# }

#Session timeout config

SESSION_EXPIRE_SECONDS = 3600  # 1 hour

SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_URL = 'static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# STATIC_ROOT = os.path.join(BASE_DIR, "static/")


MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SMTP Configuration (Its working fine, just add the mail and its password)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'gmail.googleapis.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'residencesankluxury@gmail.com'
# EMAIL_HOST_PASSWORD = "qaqqmkhnajckxboq"

PASSWORD_RESET_TIMEOUT = 14400


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]


# Locale
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

SITE_ID = 2
