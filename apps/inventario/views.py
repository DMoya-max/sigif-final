from django.shortcuts import render
from apps.productos.models import Producto

def inventario(request):

    producto = Producto.objects.all()

    contexto = {
        'producto': producto
    }


    return render(request, "inventario/inventario.html", contexto)

def inv_historial(request):

    return render(request, "inventario/inv_historial.html")

def inv_control(request):

    return render(request, "inventario/inv_control.html")

def inv_configuracion(request):

    return render(request, "configuracion/configuracion.html")
