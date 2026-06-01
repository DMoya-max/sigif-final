from django.urls import path
from . import views
urlpatterns = [
    path('configuracion/', views.configuracion, name='configuracion'),
    path('backupypermisos/', views.backupypermisos, name='backupypermisos'),

]
