from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout,login,authenticate
from .forms import CustomUserCreationForm 
from .forms import *
import time
from django.db.models import Q
from .models import *

from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def Home(request):
    ver=Producto.objects.all().order_by('Codigo')[:4]
    data={
        'a':ver
    }
    return render (request, "index.html",data)

@login_required


def Salir(request):
    logout(request)
    return redirect('Home')


def Buscar(request):
    data = {
        'buscarform': ProductoForm()
    }
    if request.GET.get('buscar'):
        buscar = request.GET.get('buscar')
        data['productos'] = Producto.objects.filter(
            Q(nombre__icontains=buscar) | Q(descripcion__icontains=buscar)
        )
    else:
        data['productos'] = Producto.objects.all()
    return render(request, 'Pages/Buscar.html', data)


def Register(request):
    data = {
        'signup': CustomUserCreationForm()
    }
    query = CustomUserCreationForm(data=request.POST)
    if query.is_valid():
        query.save()
        user = authenticate(username=query.cleaned_data['username'],
                            password=query.cleaned_data['password1'])
        login(request, user)
        data["mensaje"] = "mati mete el script aca"
        time.sleep(1)
        return redirect('Home')
    data['form'] = query
    return render(request, 'registration/register.html', data)

def producto(request):
    query= Producto.objects.all()
    filtroNom = request.GET.get('filtroNom')
    filtroDes = request.GET.get('filtroDes')
    if filtroNom:
        query=Producto.objects.filter(
            Q(Nombre__icontains=filtroNom) |
            Q(Descripcion__icontains=filtroDes)
        )
    else:
        query = Producto.objects.all()
    data={
        'productos':query
    }
    return render(request,"pages/Productos.html", data)

@staff_member_required

def Registro(request):
    query = Producto.objects.all()
    data={
        'productos': query,
        'regproducto':ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Producto agregado correctamente"
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
            return redirect('Registro')

    return render(request, 'Pages/Modificar.html', data)

def eliminar_producto(request, codigo):
    producto = Producto.objects.get(Codigo=codigo)
    producto.delete()
    return redirect('Registro')




