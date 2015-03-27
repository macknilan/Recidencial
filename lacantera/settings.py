"""
Django settings for lacantera project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<< HEAD
SECRET_KEY = os.environ["SECRET_KEY"]
=======
>>>>>>> 198cb3a2a6c4cd3667a2a48adad1ea88dce77ce1
# SECURITY WARNING: don't run with debug turned on in production!

DATE_FORMAT = '%d-%m-%Y'

DATE_INPUT_FORMATS = '%d-%m-%Y'

# _PARA PRODUCCION_
# 
# DEBUG = False
# TEMPLATE_DEBUG = DEBUG
# 
# PARA NO PEGARLE TAN DURO A LA b.d. 
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache_db'
# 
# A UN MAS -- SI NO NOS IMPORTA QUE SE PIERDA LA SESION
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache' 
# 

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

USE_THOUSAND_SEPARATOR = True

# NUMBER_GROUPING = 1

THOUSAND_SEPARATOR = ','

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lacantera',
    'casagenerales',
    'casamovimientos',
    'compradores',
    'userprofiles',
    'storages',
    # 'mockups',
    # 'django_extensions',
)

MIDDLEWARE_CLASSES = (
    # 'django.middleware.cache.UpdateCacheMiddleware', HABILITAR EN PRODUCCION
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.cache.FechFromCacheMiddleware', HABILITAR EN PRODUCCION
)

# CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True HABILITAR EN PRODUCCION

ROOT_URLCONF = 'lacantera.urls'

WSGI_APPLICATION = 'lacantera.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lacanteradb',
        'USER': 'lacanterauser2015',
        'PASSWORD': 'veHEeRC2bwuqCJy',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-mx'
# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'lacantera/static'),
#)

# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'  # PARA PONER CACHE LOS ARCHIVOS ESTATICOS EN PRODUCCION

# STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['static'])  # PARA PONER CACHE LOS ARCHIVOS ESTATICOS EN PRODUCCION

# STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
 )  # PARA PONER CACHE LOS ARCHIVOS ESTATICOS EN PRODUCCION


#MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#MEDIA_URL = '/media/'

# AUTH_USER_MODEL = "userprofiles.UserProfile"

<<<<<<< HEAD
##### AWS SETTINGS

AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
=======

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

STATICFILES_STORAGE = 'custom_storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)


###### END AWS SETTINGS
