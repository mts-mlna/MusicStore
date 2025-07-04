from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q

# Create your views here.
def Home(request):
    return render (request, "index.html")

def RegistrarProducto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        imagen = request.FILES.get('imagen')

        producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, stock=stock, imagen=imagen)
        producto.save()

    return render()

def RegistrarCliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')

        cliente = Cliente(nombre=nombre, apellido=apellido, email=email, telefono=telefono)
        cliente.save()

    return render()