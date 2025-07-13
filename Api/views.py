from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout,login,authenticate
from .forms import CustomUserCreationForm 
from .forms import *
import time
from django.db.models import Q
from .models import *
from django.contrib import messages

from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def Home(request):
    ultimos_productos = Producto.objects.order_by('-Codigo')[:3]
    low_stock_count = Producto.objects.filter(Stock__lt=5).count()
    data = {
        'ultimos': ultimos_productos,
        'low_stock_count': low_stock_count
    }
    return render (request, "index.html",data)

@login_required


def Salir(request):
    logout(request)
    return redirect('Home')


from django.contrib import messages

def Register(request):
    if request.method == "POST":
        query = CustomUserCreationForm(data=request.POST)
        if query.is_valid():
            query.save()
            user = authenticate(username=query.cleaned_data['username'],
                                password=query.cleaned_data['password1'])
            login(request, user)
            return redirect('Home')
        else:
            for field, errors in query.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        query = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'signup': query})


def producto(request):
    query= Producto.objects.all()
    filtroNom = request.GET.get('filtroNom')
    filtroDes = request.GET.get('filtroDes')

    condiciones = Q()
    if filtroNom:
        condiciones |= Q(Nombre__icontains=filtroNom)
    if filtroDes:
        condiciones |= Q(Descripcion__contains=filtroDes)
    
    if condiciones:
        query = query.filter(condiciones)

    return render(request, "pages/Productos.html", {"productos": query})

@staff_member_required

def Registro(request):
    query = Producto.objects.order_by('-Codigo')
    data={
        'productos': query,
        'regproducto':ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto agregado correctamente")
        else:
            data['regproducto'] = ProductoForm()
    return render(request, 'Pages/Registro.html', data)

def Modificar(request, codigo):
    producto = Producto.objects.get(Codigo=codigo)
    data = {
        'modproducto': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente!")
            return redirect('Registro')

    return render(request, 'Pages/Modificar.html', data)

def eliminar_producto(request, codigo):
    producto = Producto.objects.get(Codigo=codigo)
    producto.delete()
    messages.success(request, "¡Eliminado correctamente!")
    return redirect('Registro')
