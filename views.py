from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
#from productos.models import Producto

# 
# def index(request):
#     latest_question_list = Producto.objects.order_by('-fecha')[:5]
#     output = ', '.join([p.question_text for p in latest_question_list])
#     return HttpResponse(output)



def index(request):
    #return HttpResponse("Hello, world. index.")
    return render(request, 'index.html')