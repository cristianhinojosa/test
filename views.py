from django.http import HttpResponse

from productos.models import Producto

# 
# def index(request):
#     latest_question_list = Producto.objects.order_by('-fecha')[:5]
#     output = ', '.join([p.question_text for p in latest_question_list])
#     return HttpResponse(output)



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
