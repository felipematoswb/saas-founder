"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import logging
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com', cast=str)
EMAIL_PORT = config('EMAIL_PORT', default='587', cast=str)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_USE_SSL = config('EMAIL_USE_SSL', default=False, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default=None, cast=str)
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default=None, cast=str)

ADMINS = [('Felipe', 'felipematoswb@gmail.com')]
MANAGERS = ADMINS

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY', cast=str)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DJANGO_DEBUG', cast=bool)

ALLOWED_HOSTS = ['.railway.app']

if DEBUG:
    ALLOWED_HOSTS += ['127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'visits.apps.VisitsConfig',
    'commando.apps.CommandoConfig',
    # third party apps
    "allauth_ui",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    "widget_tweaks",
    'slippers',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",

]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DJANGO_CONN_MAX_AGE = config('DJANGO_CONN_MAX_AGE', default=30, cast=int)
DJANGO_DATABASE_URL = config('DJANGO_DATABASE_URL', default=None, cast=str)

if DJANGO_DATABASE_URL:

    try:
        import dj_database_url
        DATABASES = {
            'default': dj_database_url.config(default=DJANGO_DATABASE_URL, conn_health_checks=True, conn_max_age=30)
        }
    except ImportError as e:
        logging.error(
            "dj_database_url could not be imported. Default database configuration will not be set.")
    except Exception as e:
        logging.error(f"An error occurred while configuring the database: {e}")


# Django AllAuth Config
ALLAUTH_UI_THEME = "dim"
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_SUBJECT_PREFIX = "WholeSales - "
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = [
    # ...
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
    # ...
]

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    "github": {
        # For each provider, you can choose whether or not the
        # email address(es) retrieved from the provider are to be
        # interpreted as verified.
        "VERIFIED_EMAIL": True
    },
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_BASE_DIR = BASE_DIR / 'staticfiles'

STATICFILES_BASE_DIR.mkdir(exist_ok=True, parents=True)

STATICFILES_VENDOR_DIR = STATICFILES_BASE_DIR / 'vendors'

STATICFILES_DIRS = [STATICFILES_BASE_DIR]

STATIC_ROOT = BASE_DIR.parent / 'local-cdn'

STORAGES = {
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SILENCED_SYSTEM_CHECKS = ["slippers.E001"]
