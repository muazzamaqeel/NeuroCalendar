# calendarbackend/settings/base.py

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # Points to 'calendarbackend/'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')

# We'll default DEBUG to False; dev/prod files can override this.
DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your custom apps
    # If each has apps.py with a config class, you can do:
    # 'app.accounts.apps.AccountsConfig',
    # 'app.events.apps.EventsConfig',

    # OR, simply reference the package if you prefer:
    'app.accounts',
    'app.events',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'calendarbackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # If you have a separate templates directory:
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

WSGI_APPLICATION = 'calendarbackend.wsgi.application'
ASGI_APPLICATION = 'calendarbackend.asgi.application'

# Database: placeholders, dev/prod will override
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'placeholder',
        'USER': 'placeholder',
        'PASSWORD': 'placeholder',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Password validation (you can tweak or remove these for dev)
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files (if you have file uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
