from django.contrib import admin
#from usuarios.models import Usuario 
from productos.models import Producto, Pregunta, Respuesta

admin.site.register(Producto)
admin.site.register(Pregunta)
admin.site.register(Respuesta)