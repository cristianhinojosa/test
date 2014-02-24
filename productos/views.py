

from django.http import HttpResponse
from productos.models import Producto
from django.shortcuts import get_object_or_404, render, render_to_response



def index(request):
    latest_question_list = Producto.objects.all().order_by('-fecha')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'productos/index.html', context)




def detalle(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'productos/detalle.html', {'producto': producto })



#def busqueda(request):
    #return render(request, 'search_form.html')


def busqueda(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        productos = Producto.objects.filter(nombre__icontains=q)
        return render(request, 'productos/busqueda.html',
            {'productos': productos, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')



