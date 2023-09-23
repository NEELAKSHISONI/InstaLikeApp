from pathlib import Path
import os
from django.core.management.utils import get_random_secret_key

SECRET_KEY = get_random_secret_key()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Adjust the number of `parent` calls according to your directory structure

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'myfrontend', 'build', 'static')]

# Add this line for collecting static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# settings.py
ALLOWED_HOSTS = ['*']


REDIS_HOST = 'localhost'
REDIS_PORT = 6379


import os
import boto3

# Configure the default storage backend
AWS_ACCESS_KEY_ID = 'DO00NRUZHAX2CQ9HYPGN'
AWS_SECRET_ACCESS_KEY = 'Y8TBHvne51WDE+t4GhysR+ihWvkT6oM0czEJyxa+oxk'
AWS_STORAGE_BUCKET_NAME = 'photobucket'
AWS_S3_ENDPOINT_URL = 'https://photobucket.sfo3.digitaloceanspaces.com'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.photobucket.sfo3.digitaloceanspaces.com'

# Use this if you want to serve static files from DigitalOcean Spaces
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Use this for serving media files from DigitalOcean Spaces
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Set this to True if you want to use secure (HTTPS) URLs for your assets
AWS_S3_SECURE_URLS = False

DEBUG = True
LOGIN_REDIRECT_URL = '/dashboard/'  # Change this to the desired URL



# Set this to the directory where your media files will be stored within the bucket
AWS_LOCATION = 'media'

# Use S3 for storing static files as well (optional)
# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

# Use this if you want to serve media files using Django during development
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'

# Use this if you want to serve static files using Django during development
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'



# Other settings...

# Use the new app name here
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'channels',
    'storages',
    'corsheaders',
    'instaapp',  # Use the new app name here
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Other settings...



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]


ROOT_URLCONF = 'MyInstaLikeApp.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'myfrontend', 'build'),
            os.path.join(BASE_DIR, 'MyInstaLikeApp', 'templates')
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



ASGI_APPLICATION = 'MyInstaLikeApp.asgi.application'



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'defaultdb',
        'USER': 'doadmin',
        'PASSWORD': 'AVNS_uFeWT1BVIz8Uuua9tqE',  # Replace with your actual password
        'HOST': 'db-postgresql-sfo3-43785-do-user-14562213-0.b.db.ondigitalocean.com',
        'PORT': '25060',
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}


# settings.py

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://chathistoryredis-do-user-14562213-0.b.db.ondigitalocean.com:25061/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"




# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': ['rediss://default:AVNS_VePqOdgNdEIZ1QLFgKY@chathistoryredis-do-user-14562213-0.b.db.ondigitalocean.com:25061'],
        },
    },
}




# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ALLOW_ALL_ORIGINS = True

