from django.conf.urls import patterns, url

import views

from django.core import urlresolvers

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<producto_id>\d+)/$', views.detalle, name='detalle'),
   
    
    url(r'^busqueda/$', views.busqueda),
    #url(r'^agregar/$', views.AgregarProducto, name='agregar_producto'),
    url(r'^agregar/$', views.AgregarProductoView.as_view(), name='agregar_producto'),
    
)
