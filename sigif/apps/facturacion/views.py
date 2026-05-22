from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Factura, Cliente

class FacturaListView(ListView):
    model = Factura
    template_name = 'facturacion/facturacion.html'
    context_object_name = 'facturas'

class FacturaDetailView(DetailView):
    model = Factura
    template_name = 'facturacion/facturacion.html'
    context_object_name = 'factura'

def clientes_view(request):
    clientes = Cliente.objects.all()
    return render(request, 'facturacion/cliente.html', {'clientes': clientes})


