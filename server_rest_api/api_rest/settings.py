"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021

Usage:

    python manage.py runserver 0:9000
    or rest_api_server_start.sh

"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True

# Data connection, configure here all params
THIS_SERVER_IP='192.168.43.110'
SERVER_IP = 'http://0.0.0.0'
SERVER_PORT = ':9000'
REST_API_SERVICE_URL = SERVER_IP + SERVER_PORT
REST_API_ROOT = 'v1/'  # Change the version of REST API here
ROOT_URLCONF = 'api_rest.urls'
STATIC_URL = '/static/'
WSGI_CONF = 'api_rest.wsgi.application'
# -----------------------
# In Linux use $ echo "a_password_to_set" | sha256sum
SECRET_KEY = '0d235b95999cdad00e4da9a48b9e85f7cec377712232785df16b44b094c340c0'
# Configuration of secret keys
# ---
# If you want change the secret keys values, you must change in /src/initial_data_values/oauth2_provider.json in fields:
# client_id and client_secret
CLIENT_IDENTIFIER_STR = 'super_secret_key_id.0#'
CLIENT_SECRET = 'super_secret_client_1234567891011121314151617181920.*#super_secret_client_1234567891011121314151617181920.*#'

# language settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# configure here IP
ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', THIS_SERVER_IP, 'localhost']
CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth2_provider',
    'rest_framework',
    'src.users',
    'corsheaders',
    'django_extensions',
    'src.control_panel',
    'src.clients'
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

OAUTH2_PROVIDER = {
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

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
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'broadcast.db.sqlite3'),
    }
}


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
