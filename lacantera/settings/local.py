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

# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'  # PARA PONER CACHE LOS ARCHIVOS ESTATICOS EN PRODUCCION
# STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['static'])  # PARA PONER CACHE LOS ARCHIVOS ESTATICOS EN PRODUCCION
STATIC_URL = '/static/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])
MEDIA_URL = '/media/'


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
 )  # PARA PONER CACHE LOS ARCHIVOS ESTATICOS EN PRODUCCION


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


















































































