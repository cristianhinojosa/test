from django import forms 
from datetime import date

from django.forms import extras
import datetime

from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm  
from productos.models import Producto
from django.forms.models import ModelForm
    

yearNow = datetime.date.today().year 

class AuthorForm(forms.Form):
    nombre = forms.CharField(required=True)