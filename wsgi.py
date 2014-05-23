"""
WSGI config for website project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
#import os
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)


#!/usr/bin/python
#import os, sys
#sys.path.append('/var/www/django/test')
#os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()



import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")


# activate venv
#activate_this = ''

path_to_my_site = '/var/www/django/env/'
activate_this = os.path.join(path_to_my_site, "bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

# insert project path to sys path
sys.path.append('/var/www/')
sys.path.append('/var/www/django/test')

path = '/var/www/django/test/'
if path not in sys.path:
    sys.path.insert(0, path)

import django.core.handlers.wsgi
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = django.core.handlers.wsgi.WSGIHandler()
