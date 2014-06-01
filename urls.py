from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index
import settings
#from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf.urls.static import static
#from distutils.command.register import register
#from django.core.urlresolvers.reverse

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    
     url(r'^$', index, name='index'),
     url(r'^usuarios/', include('accounts.urls') ),
     url(r'^productos/', include('productos.urls', namespace='productos')),
     url(r'^chorizo/', include(admin.site.urls)),
     url(r'^accounts/', include('registration.backends.default.urls')),
     url(r'^i18n/', include('django.conf.urls.i18n')),
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
     #url(r'^static/(?P<path>.*)$', 'serve'),
     #url(r'^pages/', include('django.contrib.flatpages.urls')),
     #url(r'^media/static/bootstap/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
