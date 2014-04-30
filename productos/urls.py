from django.conf.urls import patterns, url

from productos import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<producto_id>\d+)/$', views.detalle, name='detalle'),
    url(r'^agregar/$', views.agregar_producto, name='agregar_producto'),
    
    url(r'^busqueda/$', views.busqueda),
    
    # ex: /polls/5/results/
    #url(r'^(?P<producto_id>\d+)/results/$', views.resultado, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<producto_id>\d+)/vote/$', views.vote, name='vote'),
)
