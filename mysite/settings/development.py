
from .base import *
import os,secrets

# SECRET_KEY

SECRET_KEY = os.getenv('SECRET_KEY')
if SECRET_KEY == None:
    os.environ["SECRET_KEY"] = secrets.token_urlsafe(32)
    SECRET_KEY = os.getenv('SECRET_KEY')


DEBUG = True

#Development Code below not needed for prod
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
devip = '127.0.0.1'
port = 8000
try:
    s.connect(('8.8.8.8',80))
    devip = s.getsockname()[0]
except:
    print('couldnt connect, defaulting to 127.0.0.1')
    pass
_host = f'{devip}:{port}'
# end of dev code
#modify the below variables for production

ALLOWED_HOSTS = [devip,'127.0.0.1','localhost']


CSRF_TRUSTED_ORIGINS=[
        'http://localhost:8080',
        'http://' + _host,

        ]


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
        'default':{
            'ENGINE':'django.db.backends.sqlite3',
            'NAME':'sqlite3.db'
            },
    'main_default': {    
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('PGDATABASE'),
        'USER':  os.getenv('PGUSER'),
        'PASSWORD': os.getenv('PGPASSWORD'),
        'HOST': os.getenv('PGHOST'),
        'PORT': os.getenv('PGPORT'),

                'TEST':{
        'ENGINE':'django.db.backends.sqlite3',
        'NAME':'testdatabase.db',
        }
                }
}




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = '/data/data/com.termux/files/usr/var/www/mysite/static'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# EMAILING SETTINGS

EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
