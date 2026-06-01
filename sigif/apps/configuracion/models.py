
from django.db import models

class EmpresaConfig(models.Model):
    nombre_comercial = models.CharField(max_length=150, default="SIGIF")
    nit = models.CharField(max_length=50, default="900.123.456-7")
    direccion = models.CharField(max_length=255, default="CASA DE MOYA \"LA AURORA\" ")
    moneda = models.CharField(max_length=50, default="COP ($) - Pesos Colombianos")
    impuesto = models.CharField(max_length=10, default="19%")
    correo_contacto = models.EmailField(default="soporte@sigif.com")

    def __str__(self):
        return self.nombre_comercial