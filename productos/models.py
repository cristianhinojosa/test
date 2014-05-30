# -*- encoding: utf-8 -*-

from datetime import date, timedelta, datetime
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
from django.utils import timezone
import datetime



ESTADOS_PRODUCTO = (
     ('Nuevo', _('Nuevo')),
     ('Usado', _('Usado')),
 )


ESTADOS_PUBLICACION = (
     ('revisando', _('Revisando')),
     ('publicado', _('Publicado')),
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

#fecha_termino = timezone.now() + datetime.timedelta(days=60)

#ahora2 = datatime.now()

#d = datetime

DESTACAR = (
       ('si', _('1')),
       ('no', _('0')),
            )

future_days  = timezone.now() + datetime.timedelta(days=90)
now = timezone.now()
#print ahora


class Producto(models.Model):
    def validate_image(self):
        filesize = self.file.size
        megabyte_limit = 1.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("La imagen debe pesar como maximo %sMB" % str(megabyte_limit))

    
    
    nombre =  models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    valor = models.PositiveIntegerField(default=1,  null=True, blank=True)
    estado_producto = models.CharField(max_length=200,choices=ESTADOS_PRODUCTO, null=True, blank=True)
    estado_publicacion = models.CharField(max_length=200,choices=ESTADOS_PUBLICACION, null=True, blank=True)
    region = models.CharField(max_length=200,choices=REGION_CHOICES,  null=True, blank=True)
    usuario = ForeignKey(User,  null=True, blank=True, editable=False) 
    fecha_inicio = models.DateTimeField(default=now, editable=False)
    fecha_termino = models.DateTimeField(default=future_days, editable=False)
    destacar = models.CharField(max_length=200,choices=DESTACAR, null=True, blank=True)
    
    categorias = models.CharField(max_length=200,choices=CATEGORIAS, null=True, blank=True)
    

    imagen_1 = models.ImageField("1 foto", upload_to="images/productos", blank=True, validators=[validate_image])
    #imagen_2 = models.ImageField("2 foto", upload_to="images/productos", blank=True)
    #imagen_3 = models.ImageField("3 foto", upload_to="images/productos", blank=True)
    #imagen_4 = models.ImageField("4 foto", upload_to="images/productos", blank=True)
    #imagen_5 = models.ImageField("5 foto", upload_to="images/productos", blank=True)
    
    def __unicode__(self):
        return self.nombre


class Pregunta(models.Model):
    
    
    usuario = ForeignKey(User,  null=True, blank=True, editable=False)
    producto = ForeignKey(Producto,  null=True, blank=True) 
    pregunta =  models.CharField(max_length=200, null=True, blank=True)
    
    def __unicode__(self):
        return self.pregunta

class Respuesta(models.Model):
    #usuario = ForeignKey(User,  null=True, blank=True, editable=False) 
    #pregunta = models.OneToOneField(Pregunta)
     
    
    #pregunta = ForeignKey(Pregunta,  null=True, blank=True)
    pregunta = models.OneToOneField(Pregunta)
    #producto = ForeignKey(Producto,  null=True, blank=True, editable=False)
    respuesta =  models.CharField(max_length=200, null=True, blank=True)
    
    def __unicode__(self):
        return self.respuesta
    
    
    

    