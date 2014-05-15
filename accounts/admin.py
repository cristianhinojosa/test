from django.contrib import admin
from accounts.models import UserProfile


#from usuarios.models import Usuario

#from productos.models import Producto 



class UsuarioAdmin(admin.ModelAdmin):
    #fields = ['nombre', 'email']

    list_display = ('direccion', 'telefono_fijo','celular')
    search_fields = ['email']



admin.site.register(UserProfile)