#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth import login, authenticate, logout
#from django.contrib.auth.decorators import login_required
#from django.shortcuts import get_object_or_404, render, render_to_response

#def nuevo_usuario(request):
#	if request.method == 'POST':
#		form = UserCreationForm(request.POST)
#			if form.is_valid():
#				user = form.save()
#				return HttpResponseRedirect('/')
#
#	else:
#		form = UserCreationForm()	
#	return render_to_responsive('usuarios/nuevousuario.html', {'form':form}, context_instance=RequestContext(request)))
	
from django.shortcuts import render
from django.http import HttpResponseRedirect    
from django.contrib import auth                 
from django.core.context_processors import csrf 
from .forms import MyRegistrationForm


from django.contrib.auth.decorators import login_required

@login_required
def opciones(request):

	pass

def send_registration_confirmation(user):
	p = user.get_profile()
	title = "Gsick account confirmation"
	content = "http://www.gsick.com/confirm/" + str(p.confirmation_code) + "/" + user.username
	send_mail(title, content, 'no-reply@gsick.com', [user.email], fail_silently=False)



def agregar(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)     # create form object
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/usuarios/opciones')
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    print args
    return render(request, 'nuevousuario.html', args)
