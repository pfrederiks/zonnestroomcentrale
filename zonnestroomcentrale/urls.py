from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.auth.views import login, logout



from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
	(r'^$', 'direct_to_template', {'template' : 'index.html', 'extra_context':{'section' : "introduction"}}),
	(r'^about/$','direct_to_template', {'template' : 'about.html', 'extra_context':{'section' : "about"}} ),
	(r'^prizes/$','direct_to_template', {'template' : 'prizes.html', 'extra_context':{'section' : "prizes"}} ),
	(r'^questionnaire/thanks/$','direct_to_template', {'template' : 'questionnaire/thanks.html', 'extra_context':{'section' : "questionnaire"}}),
	)
	
urlpatterns += patterns('zonnestroomcentrale.accounts.views',
		(r'^accounts/profile/$','profile'),
		(r'^accounts/register/$','register'),
		(r'^accounts/login/$','login'),	
		  )
	
urlpatterns += patterns('',
	# existing patterns here...
	(r'^accounts/logout/$', logout),
		 
)

urlpatterns += patterns('zonnestroomcentrale.questionnaire.views',
	(r'^questionnaire/$', 'index'),
	)
	
urlpatterns += patterns('',
	(r'^i18n/', include('django.conf.urls.i18n')),
	 (r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^admin/(.*)', admin.site.root),
)
		
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

