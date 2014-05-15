from django import forms 
from datetime import date

from django.forms import extras
import datetime

#from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm      
from accounts.models import UserProfile
from django.contrib.auth.models import User

#from usuarios.models import Usuario


yearNow = datetime.date.today().year 


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = False)
    last_name = forms.CharField(required = False)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')        

    def save(self,commit = True):   
        user = super(MyRegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        
        if commit:
            user.save()

        return user
    

#class Perfil(forms):
    #direccion = forms.CharField(required = True)
    #telefono_fijo = forms.CharField(required = False)
    #celular = forms.CharField(required = False)
    
    
    #user.telefono_fijo = self.cleaned_data['telefono_fijo']
    #user.celular = self.cleaned_data['celular']
    #direccion = forms.CharField(required = False)
    
#    telefono_fijo =  forms.IntegerField(required = True)
#    celular =  forms.IntegerField(required = True)





