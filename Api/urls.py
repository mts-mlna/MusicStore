from django.urls import path
from .views import *

urlpatterns = [
    path('',Home, name='Home'),
    # path('administrador/', Administrador, name='administrador'),
    path('logout/', Salir, name='logouts'),
    path('register/', Register, name='Register'),
    path('Registro/', Registro, name='Registro'),
    path('Buscar/', Buscar, name='Buscar'),
    path('Producto/', producto, name='Producto'),
    path('Modificar/<int:codigo>/', Modificar, name='Modificar'),
    path('eliminar_producto/<int:codigo>/', eliminar_producto, name='eliminar_producto'),
]