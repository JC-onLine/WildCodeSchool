"""
Django settings for project_cfg project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os, json
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ==== BEGIN CUSTOM ENV ====
# Get DJANGO Setup from private JSON file: If 'None' go to local dev mode.
SECURE_ZONE = os.path.join(BASE_DIR, '..', 'secure-zone')
DJANGO_ENV = os.path.join(SECURE_ZONE, 'django-env.json')
try:
    with open(DJANGO_ENV, 'r') as django_env:
        settings_data = django_env.read()
    settings_obj = json.loads(settings_data)    # pars to JSON object
    # Get DJANGO ENV from JSON file:
    DJANGO_URL = str(settings_obj['DJANGO_URL'])
    DJANGO_DEBUG = str(settings_obj['DJANGO_DEBUG'])
    DJANGO_KEY = str(settings_obj['DJANGO_KEY'])
except IOError as err:
    # No DJANGO ENV from JSON file or force to DEV mode:
    print(f"==== /!\\ ==== Settings.py: File IOError {err}")
    print(f"==== /!\\ ==== Settings.py: FORCE DEVELOPMENT MODE")
    DJANGO_URL = '127.0.0.1'
    DJANGO_DEBUG = True
    DJANGO_KEY = '=u+udiqp%x@g$0-w9=82i3*g6tl-edrdvpzbpqo$^nz@&&jrit'
# #### END CUSTOM ENV ====



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = DJANGO_KEY

# SECURITY WARNING: don't ws_sender_run with debug turned on in production!
# Custum: Add DEBUG and DJANGO_URL info in environment OS:
DEBUG = DJANGO_DEBUG

ALLOWED_HOSTS = [
    '127.0.0.1',
    DJANGO_URL,
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'argonautes.apps.ArgonautesConfig',
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

ROOT_URLCONF = 'project_cfg.urls'

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

WSGI_APPLICATION = 'project_cfg.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# ==== TEST DEV/PROD ENV ====
# PROD ENV
if os.path.isfile(BASE_DIR / '..' / 'secure-zone' / 'db.sqlite3'):
    sqlite = BASE_DIR / '..' / 'secure-zone' / 'db.sqlite3'
    print(f"==== Settings.py: PRODUCTION DATABASE")
else:
    sqlite = BASE_DIR / 'db.sqlite3'
    print(f"==== /!\\ ==== Settings.py: DEVELOPMENT DATABASE")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': sqlite,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# ==== CUSTOM PROJECT SECTION ====

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# Static Django with 'manage.py collectstatic'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Display settings.py details
print(f"==== settings.py: ALLOWED_HOSTS={ALLOWED_HOSTS}")
print(f"==== settings.py: DEBUG={DEBUG}")
print(f"==== settings.py: SECRET_KEY={SECRET_KEY}")
