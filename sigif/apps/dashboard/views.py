from django.shortcuts import render
from apps.usuarios.models import Usuarios
from apps.productos.models import Producto
from django.http import JsonResponse

def index(request):
    total = Usuarios.objects.count()
    to = Producto.objects.count()

    context = {
        'total': total,
        'to': to
    }

    return render(request, 'dashboard/index.html', context)

def mant(request):

    return render(request, "mant.html")
