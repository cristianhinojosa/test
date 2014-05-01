
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from productos.models import Producto
from django.shortcuts import get_object_or_404, render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from forms import ProductoForm
from django.core.urlresolvers import reverse_lazy



def index(request):
    latest_question_list = Producto.objects.all().order_by('-fecha')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'productos/index.html', context)




def detalle(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'productos/detalle.html', {'producto': producto })




def agregar_producto (TemplateView):  
    template_name = 'productos/agregar.html'
        
        if self.request.method == 'POST':
            form_kwargs['data'] = self.request.POST
        
        producto_form = ProductoForm(prefix='producto', **form_kwargs)
        kwargs['productos_form'] = producto_form
        return kwargs
    

    #return render_to_response('budget_request/budget-request-success.html', {'producto_form': producto_form}, context_instance=RequestContext(self.request))
    
    #return self.render_to_response(context)    
    
    
    #if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
    #    form = ProductoForm(request.POST) # A form bound to the POST data
    #    if form.is_valid(): # All validation rules pass
    #        # Process the data in form.cleaned_data
            # ...
    #        return HttpResponseRedirect('/thanks/') # Redirect after POST
    #else:
    #    form = ProductoForm() # An unbound form

    #return render(request, 'productos/agregar.html', {
    #    'form': form,
    #})


    
def busqueda(req):
    if req.GET:
        q = req.GET['q']
        results = Producto.objects.filter(nombre=q)
	       #return HttpResponse('No se encontraron Productos')

        return render_to_response('productos/search.html', {'results': results})
    else:
        return HttpResponse('Please submit a search term.')
    
    return render_to_response('productos/search.html', {})


