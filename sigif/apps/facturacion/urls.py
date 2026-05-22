from django.urls import path
from . import views

urlpatterns = [
    path('', views.FacturaListView.as_view(), name='facturacion'),
    path('facturas/', views.FacturaListView.as_view(), name='factura-list'),
    path('facturas/<int:pk>/', views.FacturaDetailView.as_view(), name='factura-detail'),
    path('clientes/', views.clientes_view, name='clientes'),
    path('productos/', views.productos_facturacion_view, name='productos_facturacion'),
]