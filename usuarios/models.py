from django.db import models
from django.db.models.fields import EmailField
from django.contrib.auth.models import User
#from django.utils.translation import ugettext_lazy as _



class Usuario(User):
    #email = EmailField(primary_key=True)
    #clave = models.CharField(max_length=50)
    #nombre =  models.CharField(max_length=200)
    #apellido =  models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono_fijo = models.IntegerField()
    celular = models.IntegerField()
 
    #def __str__(self):
    #    return '%s %s (%s)'%(self.name)
    
    #def __unicode__(self):
    #    return unicode(self.__str__()) 
    
#    def __str__(self):              # __unicode__ on Python 2
#        return (self.email, self.nombre)
