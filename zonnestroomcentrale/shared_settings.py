# Django settings for Zonnestroomcentrale project.

gettext_noop = lambda s: s

ADMINS = (
	('Paul Frederiks', 'paul.frederiks@gmail.com')
)

MANAGERS = ADMINS
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'nl'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

LANGUAGES = (
	('nl', gettext_noop('Dutch')),
	('en', gettext_noop('English'))
	)
	 
# Make this unique, and don't share it with anybody.
SECRET_KEY = '=ek$6!2dtvp4=^wm9m-5fu&0r*5ivm0gg0!$g#^i(n=_1t26(p'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'zonnestroomcentrale.urls'

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.admin',
	'zonnestroomcentrale.questionnaire',
	'zonnestroomcentrale.accounts',
)

AUTH_PROFILE_MODULE = "accounts.profile"

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.core.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.core.context_processors.request",
	"django.core.context_processors.debug"
)


