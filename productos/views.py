

from django.http import HttpResponse
from productos.models import Producto
from django.shortcuts import get_object_or_404, render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from productos.forms import ProductosForm
from django.core.urlresolvers import reverse_lazy



def index(request):
    latest_question_list = Producto.objects.all().order_by('-fecha')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'productos/index.html', context)




def detalle(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'productos/detalle.html', {'producto': producto })




def agregar_producto (FormView):

    template_name = 'productos/agregar_producto.html'
    form_class = ProductosForm
    success_url = reverse_lazy('home')
 
    # add the request to the kwargs
    def get_form_kwargs(self):
        kwargs = super(agregar_producto, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    #def form_valid(self, form):
    #   return HttpResponse('form valid')
    
    return render_to_response(template_name, {'form_class':form_class})

#def busqueda(request):
    #return render(request, 'search_form.html')


#def busqueda(request):
#    if 'q' in request.GET and request.GET['q']:
#        q = request.GET['q']
#        productos = Producto.objects.filter(nombre__icontains=q)
#        return render(request, 'productos/busqueda.html',
#            {'productos': productos, 'query': q})
#    else:
#        return HttpResponse('Please submit a search term.')


def busqueda(req):
    if req.GET:
        q = req.GET['q']
        results = Producto.objects.filter(nombre=q)
	       #return HttpResponse('No se encontraron Productos')

        return render_to_response('productos/search.html', {'results': results})
    else:
        return HttpResponse('Please submit a search term.')
    
    return render_to_response('productos/search.html', {})


