from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["LLAVESECRETA"]
# SECRET_KEY = get_env_variable('LLAVESECRETA')

DEBUG = True

TEMPLATE_DEBUG = True


INSTALLED_APPS += (
    'mockups',
    'django_extensions',
)


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

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'lacantera/static'),
)


STATIC_URL = '/static/'


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
 )  # PARA PONER CACHE LOS ARCHIVOS ESTATICOS EN PRODUCCION


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'



















































































