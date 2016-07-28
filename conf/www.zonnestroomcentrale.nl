<VirtualHost *:80>

        ServerAdmin admin@zonnestroomcentrale.nl
        ServerName www.zonnestroomcentrale.nl:80

	RPAFenable On
	RPAFsethostname On
	RPAFproxy_ips 127.0.0.1

#        WSGIDaemonProcess zonnestroomcentrale user=zonnestroomcentrale group=zonnestroomcentrale\
#                 processes=2 threads=8 stack-size=524288 maximum-requests=500 display-name=%{GROUP}
#        WSGIProcessGroup zonnestroomcentrale

        WSGIScriptAlias / /srv/zonnestroomcentrale/apache/django.wsgi

        <Directory /srv/django/apache>
                Order deny,allow
                Allow from all
        </Directory>

</VirtualHost>
