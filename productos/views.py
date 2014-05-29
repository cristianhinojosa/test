# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView

from django.http import HttpResponse
from productos.models import Producto, Pregunta, Respuesta
from django.shortcuts import get_object_or_404, render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from forms import ProductoForm
from django.core.urlresolvers import reverse_lazy
from django.template.context import RequestContext
from productos.forms import OtherProductoForm, SearchProducts, PreguntaForm
from settings import HOME, MEDIA_URL
#from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, InvalidPage,\
    PageNotAnInteger
from django.core.context_processors import request
from django.core.exceptions import ObjectDoesNotExist
import views


from django.db import connection
print connection.queries
    
#test->2.2.2.2

#from endless_pagination.decorators import 
from endless_pagination.decorators import page_template
from django.template.loader import get_template
import user
import settings
from django.core.mail import send_mail
from django.db.models.query_utils import Q

@page_template('productos/productos.html')  # just add this decorator
def buscar(request, template='productos/productos.html', extra_context=None):
    if request.GET.get('buscar') and  request.GET.get('region'): 
        buscar = request.GET['buscar']
        region = request.GET['region']
        form = SearchProducts()  
        
     
        
        
        context = {
                   #'entries': Producto.objects.all(),
                  
                   #'entries': Producto.objects.filter(nombre=buscar).filter(region=region), 
                  'entries':  Producto.objects.filter(
                                                     
                                                     Q(region__icontains=region)
                                                     & Q(nombre__icontains=buscar)
                                                     & Q(estado_publicacion__icontains="publicado")
                                                     | Q(descripcion__icontains=buscar) 
                                                    
                                                     ),
                   'form': form,
                   
                   }
        

        
    else:
        
        form = SearchProducts() # An unbound form
        #listado_productos = Producto.objects.all().order_by('-fecha')

    #return render(request, 'productos/productos.html', {
    #    'form': form,
    # 'listado_productos': listado_productos,
    #})
        return HttpResponseRedirect('/productos/listar/')  
      
    if extra_context is not None:
        context.update(extra_context)
        
    #print context    
    return render_to_response(
        template, context, context_instance=RequestContext(request))
    
      
 
        
    
#def listar(request):
@page_template('productos/productos.html')  # just add this decorator
def listar(request, template='productos/productos.html', extra_context=None):
        
        form = SearchProducts()  
        context = {
                   'entries': Producto.objects.filter(Q(
                                                        estado_publicacion__icontains="publicado")
                                                        )
                                                        .order_by('-fecha_inicio'),
                                                        #[:1000],
                   #'entries': Producto.objects.all().order_by('-fecha_inicio')[:500], 
                   'form': form,
                   }
        if extra_context is not None:
            context.update(extra_context)
        return render_to_response(
                                  template, context, context_instance=RequestContext(request))
    
      
    

def detalle(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    preguntas = Pregunta.objects.filter(producto=producto_id)
    #preguntas = Respuesta.objects.all()
        
    
    
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = PreguntaForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            pregunta = form.save(commit=False)
            pregunta.producto = producto
            pregunta.usuario = request.user
            pregunta.save()
    
    else:
        form = PreguntaForm() # An unbound form
       
        
        #preguntas = Respuesta.objects.filter(producto=producto_id)
        
        #preguntas
        #respuestas = Respuesta.objects.all()
        
        #preguntas = Pregunta.objects.all()

    #return render(request, 'productos/agregar.html', {
    #    'form': form,
    #})
    return render(request, 'productos/detalle.html', {'producto': producto, 'form':form, 'preguntas':preguntas })




        
        
def AgregarProducto(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = ProductoForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            
            producto = form.save(commit=False)
            producto.estado_publicacion = ("revisando")
            producto.usuario = request.user
            user = request.user
            producto.save()
            
            mail_context_dict = {
                     'user': user,
                     'producto': producto,
                   # 'consulting_appointment': consulting_appointment
                    #'task_suggestion_kwargs': task_suggestion_kwargs
            }
            
            
            mail_context = RequestContext(request, mail_context_dict)
            mail_template = get_template('productos/email.html')
            mail_message = mail_template.render(mail_context)
            mail_subject = 'Su publicación esta siendo revisada ' + user.first_name + ' ' + user.last_name + ', Email :' + user.email
            send_mail(mail_subject, mail_message, user.email, [user.email], settings.EMAIL_FAIL_SILENTLY)
            
        #test
        #send_mail(mail_subject, mail_message, customer.email, ['cristian.hinojosa@lingua-group.org', 'logs@lingua-group.org'], settings.EMAIL_FAIL_SILENTLY)
        
          
                   
        
            return redirect('productos:listar_productos')
            
         
            
            
        
            #producto.save()
            #return HttpResponseRedirect(HOME) # Redirect after POST
    else:
        form = ProductoForm() # An unbound form

    return render(request, 'productos/agregar.html', {
        'form': form,
    })

class AgregarProductoView(TemplateView):  
    template_name = 'productos/agregar_other.html'

        #kwargs = super(BudgetRequestView, self).get_context_data(**kwargs)
        
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if context['form'].is_valid():
            producto = context['form'].save(commit=False)
            producto.save()
            return render_to_response('productos/producto-ok.html', {'producto':producto }, context_instance=RequestContext(self.request))
        return self.render_to_response(context)
    
    def get_context_data(self, **kwargs):
        form_kwargs = {}   
        
        if self.request.method == 'POST':
            form_kwargs['data'] = self.request.POST
        kwargs = super(AgregarProductoView, self).get_context_data(**kwargs)
        form = OtherProductoForm(prefix='producto', **form_kwargs)
   
        
        kwargs['form'] = form
    
        
        return kwargs

        
       

    


