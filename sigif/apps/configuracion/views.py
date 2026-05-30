from logging import config
from urllib import request

from django.shortcuts import render

def configuracion(request):
    return render(request, 'configuracion/configuracion.html')
