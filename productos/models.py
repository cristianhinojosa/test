

from datetime import date
from django.db import models
from django.db.models.fields.related import ForeignKey
#from django.db.models.fields.related import ImageField
#from usuarios.models import Usuario
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from settings import MEDIA_ROOT
#from django.conf.global_settings import MEDIA_ROOT



ESTADO = (
     ('Nuevo', _('Nuevo')),
     ('Usado', _('Usado')),
 )


class Producto(models.Model):
    #search_fields = ['question_text']
    nombre =  models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    #fotografia = models.ImageField
    valor = models.IntegerField(default=0)
    estado = models.CharField(max_length=200,choices=ESTADO)
    user = ForeignKey(User,  unique=True) 
    #fecha = models.DateTimeField('fecha de publicacion del producto', null=False) 
    fecha = models.DateTimeField(_("Date"), auto_now_add=True, null=False)
    fotografia = models.FileField(upload_to="images/", null=True)
    #file = models.FileField(upload_to=MEDIA_ROOT, null=True)
    
    def __unicode__(self):
        return self.nombre
    
