from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Factura

class FacturaListView(ListView):
    model = Factura
    template_name = 'facturacion/facturacion.html'
    context_object_name = 'facturas'

class FacturaDetailView(DetailView):
    model = Factura
    template_name = 'facturacion/facturacion.html'
    context_object_name = 'factura'

def clientes_placeholder(request):
    return render(request, 'mant.html')

