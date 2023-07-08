from django.shortcuts import render, redirect
from .models import Vehiculo, Categoria, ContactMessage
from .forms import VehiculoForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
# def home(request):
#     vVehiculos = Vehiculo.objects.all()
#     datos = {'vehiculos':vVehiculos}
#     return render(request, 'home.html', datos)

def form_perrito(request):
    datos ={
        'form':VehiculoForm()
        }
    if request.method=='POST':
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Guardados correctamente"
    return render(request, 'form_perrito.html',datos)


def crud(request):
    vVehiculos = Vehiculo.objects.all()
    contexto = {'nombre':'Héctor y Jorge', 'vehiculos':vVehiculos}
    return render(request, 'crud.html', contexto)

def form_mod_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    datos = {
        'form':VehiculoForm(instance=vehiculo)
    }
    if request.method=='POST':
        formulario = VehiculoForm(data=request.POST,instance=vehiculo)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Registro Actualizado correctamente"
    return render(request,'form_mod_vehiculo.html', datos)

def form_del_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()
    return redirect(to="home")

def nosotros(request):
    return render(request, 'nosotros.html')

def index(request):
   
    return  redirect('inicio')

def aceite(request):
    return render(request, 'aceite.html')

def bujias(request):
    return render(request, 'bujias.html')

def pastillas(request):
    return render(request, 'pastillas.html')


def perros(request):
    return render(request, 'perros.html')


def form_contacto(request):
    return render(request, 'form-contacto.html')


@login_required
def sesion(request):
    return render(request,'sesion.html')

def salir(request):
    logout(request)
    return redirect('/')


def crearcuenta(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Usuario registrado exitosamente.")
            return redirect(to="index")
        else:
            # Agrega tu lógica de validación adicional para la contraseña aquí
            password1 = form.cleaned_data.get('password1')
            if len(password1) < 8:
                messages.error(request, "La contraseña debe tener al menos 8 caracteres.")
            if not any(char.isdigit() for char in password1):
                messages.error(request, "La contraseña debe contener al menos un número.")
            # Agrega más validaciones según tus requisitos

            # Renderiza nuevamente el formulario con los errores
            return render(request=request, template_name="crearcuenta.html", context={"register_form": form})
    else:
        form = NewUserForm()
    return render(request=request, template_name="crearcuenta.html", context={"register_form": form})



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Aquí puedes procesar los datos del formulario, como guardarlos en la base de datos, enviar un correo electrónico, etc.
            return render(request, 'respuesta.html', {'name': name, 'email': email, 'message': message})
    else:
        form = ContactForm()
    return render(request, 'form-contacto.html', {'form': form})

def respuesta(request, name, email, message):
    return render(request, 'respuesta.html', {'name': name, 'email': email, 'message': message})

def respuesta(request):
    # Lógica de la vista
    return render(request, 'respuesta.html')

def inicio(request):
    
    return render(request, 'inicio.html')