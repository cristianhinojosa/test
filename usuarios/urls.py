from django.conf.urls import patterns, url

from usuarios import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^agregar$', views.agregar, name='agregar'),
	url(r'^login/$', 'django.contrib.auth.views.login'),
	#url(r'^panel/$', views.panel_usuario, name='panel_usuario'),
    url(r'^mis_productos/$', views.listar_mis_productos, name='listar_mis_productos')
    
    #url(r'^busqueda/$', views.busqueda, name="busqueda_de_mis_productos"),
    #listar_mis_productos
    
    # ex: /polls/5/results/
    #url(r'^(?P<producto_id>\d+)/results/$', views.resultado, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<producto_id>\d+)/vote/$', views.vote, name='vote'),
)
