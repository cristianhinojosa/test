from datetime import date

from django import forms 
from django.forms import extras, widgets
import datetime
from productos import RestrictedImageField
from productos.models import Producto
from form_utils.forms import BetterModelForm
from django.core.exceptions import ValidationError




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
                #'fields': ['nombre', 'descripcion','valor', 'estado','imagen_1','imagen_2','imagen_3','imagen_4','imagen_5'],
                'fields': ['nombre', 'descripcion','valor', 'estado_publicacion','imagen_1'],
                'legend': ('producto'),
        }),
        ]
        
  




class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        #fields = ['nombre', 'descripcion', 'valor', 'estado', 'usuario', 'imagen_1', 'imagen_2','imagen_3','imagen_4','imagen_5']
        exclude = ('usuario', 'estado_publicacion')
    
        
     
#     def clean_imagen_1(self):
#          image = self.cleaned_data.get('imagen_1',False)
#          if image:
#              if image._size > 1*1024*1024:
#                    raise ValidationError("La imagen debe pesar hasta 1MB")
#              return image
#          else:
#              pass
#         
        
    
    
    
