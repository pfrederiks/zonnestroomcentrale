import os, sys
sys.path.append('/srv')
sys.path.append('/srv/zonnestroomcentrale')
os.environ['DJANGO_SETTINGS_MODULE']='zonnestroomcentrale.production_settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
