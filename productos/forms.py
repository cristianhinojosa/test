from django import forms 
from datetime import date

from django.forms import extras
import datetime
#

from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm  
from productos.models import Producto
from django.forms.models import ModelForm

from form_utils.forms import BetterModelForm
from form_utils.widgets import ImageWidget
from django.db.models.fields.files import ImageField
    

yearNow = datetime.date.today().year 

class OtherProductoForm(BetterModelForm):
    #nombre = forms.CharField(required=True)
    #descripcion = forms.CharField(required=True)
    #imagen_1=forms.ImageField(widget=ImageWidget)
    
    def __init__(self, *args, **kwargs):
        super(OtherProductoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = True
        self.fields['descripcion'].required = True
        self.fields['valor'].required = True
        self.fields['estado'].required = True
        #self.fields['imagen_1'].widget = forms.ImageField(widget=ImageWidget)
       

    class Meta:
        model = Producto
        fieldsets = [
            ('producto', {
                'fields': ['nombre', 'descripcion','valor', 'estado','imagen_1','imagen_2','imagen_3','imagen_4','imagen_5'],
                'legend': ('producto'),
        }),
        ]
        
        
#class ProductoForm(forms.ModelForm):

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        #fields = ['nombre', 'descripcion', 'valor', 'estado', 'usuario', 'imagen_1', 'imagen_2','imagen_3','imagen_4','imagen_5']
        exclude = ('usuario',)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    