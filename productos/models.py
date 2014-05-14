

from datetime import date
from django.db import models
from django.db.models.fields.related import ForeignKey
#from django.db.models.fields.related import ImageField
#from usuarios.models import Usuario
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from settings import MEDIA_ROOT
from django.forms.models import ModelForm

from usuarios.models import Usuario, User
from django.core.exceptions import ValidationError



ESTADO_PRODUCTO = (
     ('Nuevo', _('Nuevo')),
     ('Usado', _('Usado')),
 )


ESTADO_PUBLICACION = (
     ('revisando', _('Revisando')),
     ('visible', _('Visible')),
     ('oculto', _('Oculto')),
     
 )

CATEGORIA = ()


def main_text_image_name(instance, filename):
    '''
    Used to rename an uploaded main text image.
    '''
    extension = filename.split('.')[-1]
    return 'destinations/images/main-texts/' + str(instance.id) + '.' + extension


class Producto(models.Model):
    def validate_image(self):
        filesize = self.file.size
        megabyte_limit = 1.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("La imagen debe pesar como maximo %sMB" % str(megabyte_limit))

    
    
    nombre =  models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    valor = models.IntegerField(default='',  null=True, blank=True)
    estado_producto = models.CharField(max_length=200,choices=ESTADO_PRODUCTO, null=True, blank=True)
    estado_publicacion = models.CharField(max_length=200,choices=ESTADO_PUBLICACION,  null=True, blank=True)
    usuario = ForeignKey(User,  null=True, blank=True) 
    fecha = models.DateTimeField(_("Date"), auto_now_add=True, null=False)
       
    imagen_1 = models.ImageField("1 foto", upload_to="images/productos", blank=True, validators=[validate_image])
    #imagen_2 = models.ImageField("2 foto", upload_to="images/productos", blank=True)
    #imagen_3 = models.ImageField("3 foto", upload_to="images/productos", blank=True)
    #imagen_4 = models.ImageField("4 foto", upload_to="images/productos", blank=True)
    #imagen_5 = models.ImageField("5 foto", upload_to="images/productos", blank=True)
    
    def __unicode__(self):
        return self.nombre
    
    