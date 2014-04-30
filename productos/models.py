

from datetime import date
from django.db import models
from django.db.models.fields.related import ForeignKey
#from django.db.models.fields.related import ImageField
#from usuarios.models import Usuario
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from settings import MEDIA_ROOT
from django.forms.models import ModelForm
#from django.conf.global_settings import MEDIA_ROOT
#from formatChecker import ContentTypeRestrictedFileField


ESTADO = (
     ('Nuevo', _('Nuevo')),
     ('Usado', _('Usado')),
 )


def main_text_image_name(instance, filename):
    '''
    Used to rename an uploaded main text image.
    '''
    extension = filename.split('.')[-1]
    return 'destinations/images/main-texts/' + str(instance.id) + '.' + extension


class Producto(models.Model):
    nombre =  models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    valor = models.IntegerField(default=0)
    estado = models.CharField(max_length=200,choices=ESTADO)
    usuario = ForeignKey(User,  null=True, blank=True) 
    fecha = models.DateTimeField(_("Date"), auto_now_add=True, null=False)
   
    imagen_1 = models.ImageField("1 foto", upload_to="images/productos", default='', blank=True)
    imagen_2 = models.ImageField("2 foto", upload_to="images/productos", default='', blank=True)
    imagen_3 = models.ImageField("3 foto", upload_to="images/productos", default='', blank=True)
    imagen_4 = models.ImageField("4 foto", upload_to="images/productos", default='', blank=True)
    imagen_5 = models.ImageField("5 foto", upload_to="images/productos", default='', blank=True)
    
    def __unicode__(self):
        return self.nombre
    

class AgregarProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'valor', 'estado', 'usuario_id', 'fecha', 'imagen_1', 'imagen_2','imagen_3','imagen_4','imagen_5']