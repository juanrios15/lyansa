from .base import *

DEBUG = True

ALLOWED_HOSTS = ['juanrios.pythonanywhere.com']


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / get_secret('DB_NAME'),
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
EMAIL_HOST_USER =  get_secret('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_secret('EMAIL_HOST_PASSWORD')



