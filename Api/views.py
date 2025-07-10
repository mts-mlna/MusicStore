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
    return render (request, "index.html")

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
    data={
        'productos':query
    }
    return render(request,"pages/Productos.html", data)

def iniciarsesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            return render(request, 'registration/login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'registration/login.html')

def Registro(request):
    data={
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




