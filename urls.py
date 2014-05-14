from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index
import settings
#from django.conf.urls import url
from django.views.generic import TemplateView

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
    
    
     url(r'^$', index, name='home_page'),
     url(r'^usuarios/', include('usuarios.urls') ),
     url(r'^productos/', include('productos.urls', namespace='productos')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^accounts/', include('registration.urls')),
     #url(r'^pages/', include('django.contrib.flatpages.urls')),
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
     #url(r'^media/static/bootstap/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
)
