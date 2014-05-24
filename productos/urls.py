from django.conf.urls import patterns, url

import views

from django.core import urlresolvers

urlpatterns = patterns('',
   
  
   
    url(r'^producto/(?P<producto_id>\d+)/$', views.detalle, name='detalle'),
   
    url(r'^listar/$', views.listar, name='listar_productos'),
    url(r'^buscar/$', views.buscar, name='buscar_productos'),
    url(r'^agregar/$', views.AgregarProducto, name='agregar_producto'),
    url(r'^agregar_other/$', views.AgregarProductoView.as_view(), name='agregar_producto_view'),
    
)
