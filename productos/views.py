
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView

from django.http import HttpResponse
from productos.models import Producto
from django.shortcuts import get_object_or_404, render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from forms import ProductoForm
from django.core.urlresolvers import reverse_lazy
from django.template.context import RequestContext
from productos.forms import OtherProductoForm
from settings import HOME



def index(request):
    latest_question_list = Producto.objects.all().order_by('-fecha')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'productos/index.html', context)




def detalle(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'productos/detalle.html', {'producto': producto })




        
        
def AgregarProducto(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = ProductoForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            producto = form.save(commit=False)
            producto.usuario = request.user.usuario
            producto.save()
            
        
            #producto.save()
            return HttpResponseRedirect(HOME) # Redirect after POST
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

        
       

    
def busqueda(req):
    if req.GET:
        q = req.GET['q']
        results = Producto.objects.filter(nombre=q)
	       #return HttpResponse('No se encontraron Productos')

        return render_to_response('productos/search.html', {'results': results})
    else:
        return HttpResponse('Please submit a search term.')
    
    return render_to_response('productos/search.html', {})


