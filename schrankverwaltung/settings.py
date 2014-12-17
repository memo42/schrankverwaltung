"""
Django settings for schrankverwaltung project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
from ConfigParser import RawConfigParser

config = RawConfigParser()
#config.read('/home/vagrant/schrankverwaltung/schrankverwaltung/settings.ini')
config.read('/usr/local/share/schrank/schrankverwaltung/settings.ini')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('secrets','SECRET_KEY')
#SECRET_KEY = '/?}DN1U7m%o4#TRD6By/C-yFh)czS7dfP|>u%1kVDB`cHJ4;1#>.oJc9AoiG/n;q6/%q)<*_9kS$O1O{]$$u!E3zPWAmdqIh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#DEBUG = True

TEMPLATE_DEBUG = False
#TEMPLATE_DEBUG = True

#ALLOWED_HOSTS = ['*',]
ALLOWED_HOSTS = ['www.miemo.de', 
						'www.miemo.de.',]   

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'schrankverwaltung.urls'

WSGI_APPLICATION = 'schrankverwaltung.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = '/usr/local/share/schrank/main/static/'
