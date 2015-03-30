from .base import *
# from django.core.exceptions import ImproperlyConfigured

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["LLAVESECRETA"]

# def get_env_variable(var_name):
#     try:
#         return os.environ[var_name]
#     except KeyError:
#         error_msg = "Set the %s enviroment variable" % var_name
#         raise ImproperlyConfigured(error_msg)
# SECRET_KEY = get_env_variable('LLAVESECRETA')


# _PARA PRODUCCION_
# 
DEBUG = False

TEMPLATE_DEBUG = DEBUG
# 
# PARA NO PEGARLE TAN DURO A LA b.d. 
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache_db'
# 
# A UN MAS -- SI NO NOS IMPORTA QUE SE PIERDA LA SESION
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache' 

INSTALLED_APPS += (
    'storages',
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
# STATIC_URL = '/static/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])
# MEDIA_URL = '/media/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)  # PARA PONER CACHE LOS ARCHIVOS ESTATICOS EN PRODUCCION

# ----------AWS SETTINGS----------
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = 'lacantera'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

STATICFILES_STORAGE = 'custom_storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
# ----------END AWS SETTINGS----------



























