from datetime import date

from django import forms 
from django.forms import extras, widgets
import datetime
from productos import RestrictedImageField
from productos.models import Producto, REGION_CHOICES, Pregunta, Respuesta
from form_utils.forms import BetterModelForm
from django.core.exceptions import ValidationError
from django.forms.widgets import Textarea, TextInput
from django.forms.models import BaseModelFormSet
#from productos.forms import ProductoForm
#from django.contrib.localflavor.be.be_regions import REGION_CHOICES




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
        
  

class SearchProducts(forms.Form):
    buscar = forms.CharField(widget=forms.TextInput(attrs={'class' : 'buscar'}))
    region  = forms.ChoiceField(label="Regiones", choices=(REGION_CHOICES),
                                       widget=forms.Select(attrs={'class':'selector'}))
    
    
    #def __init__(self, *args, **kwargs):
    #    super(SearchProducts, self).__init__(*args, **kwargs)
    #    choices = [(pt.id, unicode(pt)) for pt in Producto.objects.all()]
    #    choices.extend(REGION_CHOICES)
    #    self.fields['regiones'].choices = choices
    

# class RespuestaForm(BaseModelFormSet):
#     def __init__(self, *args, **kwargs):
#         super(RespuestaForm, self).__init__(*args, **kwargs)
#         self.queryset = Respuesta.objects.all()

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta   

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta   

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        #fields = ['nombre', 'descripcion', 'valor', 'usuario', 'imagen_1', 'imagen_2','imagen_3','imagen_4','imagen_5']
        exclude = ('usuario', 'estado_publicacion', 'fecha_inicio', 'fecha_termino','destacar')
        #self.fields['descripcion'].widget.attrs['class'] = 'autocomplete'
        widgets = {
                   
                   
            'descripcion': Textarea(attrs={'cols': 20, 'rows': 7, 'class': 'form-control' }),
           #  'nombre': TextInput (attrs={'class': 'form-control' }),
        } 
        
   
      
        
     
#     def clean_imagen_1(self):
#          image = self.cleaned_data.get('imagen_1',False)
#          if image:
#              if image._size > 1*1024*1024:
#                    raise ValidationError("La imagen debe pesar hasta 1MB")
#              return image
#          else:
#              pass
#         
        
    
    
    
