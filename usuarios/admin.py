from django.contrib import admin

from usuarios.models import Usuario 
#from productos.models import Producto 



class UsuarioAdmin(admin.ModelAdmin):
    #fields = ['nombre', 'email']

    list_display = ('username', 'first_name','email')
    search_fields = ['email']



admin.site.register(Usuario, UsuarioAdmin)