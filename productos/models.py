# -*- encoding: utf-8 -*-

from datetime import date
from django.db import models
from django.db.models.fields.related import ForeignKey
#from django.db.models.fields.related import ImageField
#from usuarios.models import Usuario
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from settings import MEDIA_ROOT
from django.forms.models import ModelForm

#from user_profile import usuario
from django.core.exceptions import ValidationError



ESTADOS_PRODUCTO = (
     ('Nuevo', _('Nuevo')),
     ('Usado', _('Usado')),
 )


ESTADOS_PUBLICACION = (
     ('revisando', _('Revisando')),
     ('visible', _('Visible')),
     ('oculto', _('Oculto')),
     ('vendido', _('Vendido')),
     ('Comprado', _('Comprado')),
 )



REGION_CHOICES = (
                ('RM', 'Metropolitana'), 
                ('I', 'Tarapacá'),
                ('II', 'Antofagasta'),
                ('III', 'Atacama'), 
                ('IV', 'Coquimbo'),
                ('V', 'Valparaíso'),
                ('VI', "O'Higgins"),
                ('VII', 'Maule'),
                ('VIII', 'Bío Bío'),
                ('IX', 'Araucanía'),
                ('X', 'Los Lagos'),
                ('XI', 'Aysén'), 
                ('XII', 'Magallanes & Antártica'),
                ('XIV', 'Los Ríos'), 
                ('XV', 'Arica-Parinacota'),
                )

CATEGORIAS = (
              ('piezas', 'Piezas'),
              ('departamentos', 'Departamientos'),
              ('casas', 'Casas'),
              ('oficinas', 'Oficinas'),
              ('comercial', 'Comercial e industrial'),
              ('departamentos', 'Departamientos'),
              ('terrenos', 'terrenos'),
              ('bodegas', 'bodegas'),
              ('otros', 'otros inmuebles'),
              
              
              )


def main_text_image_name(instance, filename):
    '''
    Used to rename an uploaded main text image.
    '''
    extension = filename.split('.')[-1]
    return 'destinations/images/main-texts/' + str(instance.id) + '.' + extension


#class Categoria(models.Model):
#    nombre =  models.CharField(max_length=200, null=True, blank=True)
    

class Producto(models.Model):
    def validate_image(self):
        filesize = self.file.size
        megabyte_limit = 1.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("La imagen debe pesar como maximo %sMB" % str(megabyte_limit))

    
    
    nombre =  models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    valor = models.IntegerField(default=0,  null=True, blank=True)
    estado_producto = models.CharField(max_length=200,choices=ESTADOS_PRODUCTO, null=True, blank=True)
    estado_publicacion = models.CharField(max_length=200,choices=ESTADOS_PUBLICACION,  null=True, blank=True)
    region = models.CharField(max_length=200,choices=REGION_CHOICES,  null=True, blank=True)
    usuario = ForeignKey(User,  null=True, blank=True) 
    fecha_inicio = models.DateTimeField()
    categorias = models.CharField(max_length=200,choices=CATEGORIAS, null=True, blank=True)
       
    imagen_1 = models.ImageField("1 foto", upload_to="images/productos", blank=True, validators=[validate_image])
    #imagen_2 = models.ImageField("2 foto", upload_to="images/productos", blank=True)
    #imagen_3 = models.ImageField("3 foto", upload_to="images/productos", blank=True)
    #imagen_4 = models.ImageField("4 foto", upload_to="images/productos", blank=True)
    #imagen_5 = models.ImageField("5 foto", upload_to="images/productos", blank=True)
    
    def __unicode__(self):
        return self.nombre
    
    