from .base import *
import os, secrets
# SECRET KEY GENERATION
SECRET_KEY = os.getenv('SECRET_KEY')
if SECRET_KEY == None:
    os.environ["SECRET_KEY"] = secrets.token_urlsafe(32)
    SECRET_KEY = os.getenv('SECRET_KEY')
 

DEBUG = True

web_host = 'granzular.pythonanywhere.com'
ALLOWED_HOSTS = [web_host,'*']


CSRF_TRUSTED_ORIGINS=[
        'http://' + web_host,
        'https://' + web_host,

        ]


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
        'default':{
            'ENGINE':'django.db.backends.sqlite3',
            'NAME':'prod.sqlite3.db'
                                                }
}




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / '../static'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# EMAILING SETTINGS

EMAIL_HOST_USER = "granzularcodex@gmail.com"
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_TIMEOUT = 60 * 2

"""
# Cache
# Custom code. Database Cache and Cache Middleware

MIDDLEWARE.append('django.middleware.cache.UpdateCacheMiddleware')
MIDDLEWARE.append('django.middleware.cache.FetchFromCacheMiddleware')
 
CACHES = {                                                "default":{
            "BACKEND": "django.core.cache.backends.db.DatabaseCache",
            "LOCATION": "my_cache_table",
            }
        }
CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 60 * 15
CACHE_MIDDLEWARE_KEY_PREFIX = "portfolio-"
"""
