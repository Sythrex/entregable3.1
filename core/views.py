from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculo, Categoria, ContactMessage
from .forms import VehiculoForm, ContactForm, NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



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
    vehiculos = Vehiculo.objects.all()
    contexto = {'nombre':'Carlos', 'vehiculos':vehiculos}
    return render(request, 'crud.html', contexto)

def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'crud.html', {'vehiculos': vehiculos})

def eliminar_vehiculo(request, patente):
    vehiculo = get_object_or_404(Vehiculo, patente=patente)
    vehiculo.delete()
    return redirect('listar_vehiculos')
    
    


def modificar_vehiculo(request, patente):
    vehiculo = get_object_or_404(Vehiculo, patente=patente)
    form = VehiculoForm(instance=vehiculo)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('crud')
    return render(request, 'modificar_vehiculo.html', {'vehiculo': vehiculo, 'form': form})

def nosotros(request):
    return render(request, 'nosotros.html')

def index(request):
    user = request.user
    
    return  render(request, 'inicio.html',{'user': user})

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
def profile(request):
    return redirect('index')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Las credenciales son válidas, iniciar sesión
            login(request, user)
            return redirect('inicio')  # Redirige a la página de inicio después de iniciar sesión
        else:
            # Las credenciales no son válidas, mostrar mensaje de error
            error_message = 'Credenciales inválidas. Inténtalo de nuevo.'
            return render(request, 'registration/login.html', {'error_message': error_message})
    else:
        return render(request, 'registration/login.html')



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