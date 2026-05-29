from logging import config
from urllib import request

from django.shortcuts import render

# Create your views here.
# En tu views.py al guardar la configuración:
if request.method == 'POST':
    # Guardas los demás campos que sí son editables...
    config.prefijo = request.POST.get('prefijo')
    
    # El IVA y la moneda los sobreescribes tú a la fuerza por seguridad:
    config.iva_valor = 19.0
    config.divisa = 'COP'
    config.save()