from .base import *

DEBUG = False

ALLOWED_HOSTS = ['juanrios.pythonanywhere.com']


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/home/juanrios/lyansa/Lyansa/static/'


MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/juanrios/lyansa/Lyansa/media/'


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER =  'juankrios15@gmail.com'
EMAIL_HOST_PASSWORD = 'z3r4tul89'