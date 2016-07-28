from shared_settings import *
# Django settings for Zonnestroomcentrale project.

gettext_noop = lambda s: s

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'dev.db'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

MEDIA_ROOT = '../static/'

MEDIA_URL = 'http://127.0.0.1:8000/static/'

ADMIN_MEDIA_PREFIX = '/static/admin-media/'

INSTALLED_APPS += ( 'django.contrib.admindocs',)

TEMPLATE_DIRS = (
	"/home/paul/src/zonnestroomcentrale.nl/srv/zonnestroomcentrale/templates"
)



