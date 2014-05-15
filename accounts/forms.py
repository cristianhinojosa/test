from django import forms 
from datetime import date

from django.forms import extras
import datetime

#from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm      
from accounts.models import UserProfile

#from usuarios.models import Usuario


yearNow = datetime.date.today().year 


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = False)
    last_name = forms.CharField(required = False)
    #birthday = forms.DateField(required = False, widget=extras.SelectDateWidget(years=range(yearNow-100,  yearNow-18 )))
    
    direccion = forms.CharField(required = False)
    telefono_fijo =  forms.IntegerField(required = True)
    celular =  forms.IntegerField(required = True)

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'password2')        

    def save(self,commit = True):   
        user = super(MyRegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        # user.birthday = self.cleaned_data['birthday']
        user.direccion = self.cleaned_data['direccion']
        user.telefono_fijo = self.cleaned_data['telefono_fijo']
        user.celular = self.cleaned_data['celular']
        if commit:
            user.save()

        return user




