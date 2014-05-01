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
    

yearNow = datetime.date.today().year 

class ProductoForm(BetterModelForm):
    #nombre = forms.CharField(required=True)
    #descripcion = forms.CharField(required=True)
    
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        
        self.fields['nombre'].required = True
        self.fields['descripcion'].required = True
        self.fields['valor'].required = True
        self.fields['estado'].required = True
        
        

    class Meta:
        model = Producto
        fieldsets = [
            ('producto', {
                'fields': ['nombre', 'descripcion','valor', 'estado','imagen_1', ],
                'legend': ('producto'),
        }),
        ]