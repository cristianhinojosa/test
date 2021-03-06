#-*- coding: utf-8 -*-
import os


#ENDLESS_PAGINATION_DEFAULT_CALLABLE_EXTREMES = 1
#ENDLESS_PAGINATION_DEFAULT_CALLABLE_AROUNDS = 2

ENDLESS_PAGINATION_PAGE_LABEL = "pagina"
#ENDLESS_PAGINATION_PER_PAGE = 2


#from os.path import dirname, join, abspath, os
#from smtplib import SMTPAuthenticationError
#__dir__ = dirname(abspath(__file__))

#MAX_UPLOAD_SIZE = 1024880


MAX_UPLOAD_SIZE = 1024*1024

ACCOUNT_ACTIVATION_DAYS=7


#EMAIL_HOST = "localhost"
SERVER_EMAIL = 'cristian.hinojosa@gmail.com'
DEFAULT_FROM_EMAIL = 'cristian.hinojosa@gmail.com'
SEND_BROKEN_LINK_EMAILS = False 
EMAIL_SEND_CONFIRMATION = True     # Whether to send a booking confirmation mail to the customer
EMAIL_SEND_NOTIFICATION = True     # Whether to send a notification mail to the consultant
EMAIL_HOST = 'smtp.gmail.com'  # smtp host
EMAIL_USE_TLS = True 
EMAIL_PORT = 587                    # smtp port
EMAIL_HOST_USER = 'cristian.hinojosa@gmail.com' # smtp host user name
EMAIL_HOST_PASSWORD = ''  # smtp host password
EMAIL_SENDER_NAME = 'Cristian Hinojosa Site' # displayed name in the emails
EMAIL_SENDER = 'cristian.hinojosa@gmail.com'    # mail address that sends booking confirmations
EMAIL_FAIL_SILENTLY = False        # set to false for debugging

#SITE_ID = u'50c5766e62f11f41f0332e65'

DEFAULT_CHARSET = 'utf-8'
FILE_CHARSET = 'utf-8'


LANGUAGE_CODE = 'es'

LANGUAGES = (
  ('es', 'Español'),
  #('en', ('English')),
)



LOCALE_PATHS = (
    os.path.join(os.path.dirname(__file__), 'locale/'),
)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_SQL = True # show sql queries

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    #'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.core.context_processors.tz',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    
   

    
  
    
  #  'library.context_processors.project_urls',
  #  'library.context_processors.alternate_sites',
   # 'library.context_processors.dates',
   # 'library.context_processors.template_widget',
   # 'library.context_processors.destination_lists',
   # 'phone_numbers.context_processors.phone_numbers',
   # 'destinations.context_processors.countries',
)

MANAGERS = ADMINS

# DATABASES = {
#    'default' : {
#       'ENGINE' : 'django_mongodb_engine',
#       'NAME' : 'my_database'
#    }
# }


# DATABASES = {
#     'default' : {
#         'ENGINE' : 'django_mongodb_engine',
#         'NAME' : 'my_database',
#         'OPTIONS' : {
#             
#             'tz_aware' : True,
#             #'slave_okay' : True,#'network_timeout' : 42,
#         
#         }
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'proyecto_django_dev',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'sroot',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}




# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Santiago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'en-us'




#SITE_ID = (u'5387e2721d41c81fa5c3b33b')
SITE_ID = 1


# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
#MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
#MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = '127.0.0.1:8000/media/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media/')
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'media/static/')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
ADMIN_URL = '/admin/'

JPEG_ROOT = '/usr/local/include'
ZLIB_ROOT = '/usr/local/include'

HOME = 'http://127.0.0.1:8000/'

#SETTINGS_DIR = os.path.dirname(os.path.realpath(__file__))
#BUILDOUT_DIR = os.path.abspath(os.path.join(SETTINGS_DIR, '/var/www/django/test/'))
#STATIC_ROOT = os.path.join(BUILDOUT_DIR, 'static')
#STATIC_URL = '/static/'
#MEDIA_ROOT = os.path.join(BUILDOUT_DIR,  'media')
#MEDIA_URL = '/media/images/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Additional locations of static files
#STATICFILES_DIRS = (
     #"/var/www/django/test/static/",
     #  os.path.join( "static"),
#    "/var/www/django/test/static/",
      
      # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '#rjybe#wk405xksyiff$brlu+e4-ro@2og5^54#y^=*(6ls^^4'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    
    'django.middleware.locale.LocaleMiddleware',
    #'extended_flatpages.middleware.FlatpageFallbackMiddleware',
    
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

#TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#)




ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    
    os.path.join(os.path.dirname(__file__), 'templates'),
    os.path.join(os.path.dirname(__file__), 'templates/beratungstermin'),
    os.path.join(os.path.dirname(__file__), 'media/uploaded/templates'),
)







LOCALE_PATHS = (
    os.path.join(os.path.dirname(__file__), 'locale/'),
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
     'registration',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'endless_pagination',

   #'pagination',
    'bs4',
    'captcha',
    'compress',
    'cssutils',
    'django_countries',
    'filebrowser',
    'form_utils',
  #  'httpproxy',
    'south',
    'tinymce',
    'transmeta',
    'template_utils',

    
    'accounts',
    'productos',
    

)

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
