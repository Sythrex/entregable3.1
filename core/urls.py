from django.urls import path
from . import views 


urlpatterns = [
    path('',views.index,name="index"),
   
    path('inicio',views.inicio,name="inicio"),
    
    path('Nosotros',views.nosotros,name='nosotros'),

    path('aceite',views.aceite,name='aceite'),

    path('bujias',views.bujias,name='bujias'),

    path('pastillas',views.pastillas,name='pastillas'),

    path('Atenciones',views.crud,name="crud"),

    path('Misión',views.perros,name='perros'),

    path('sesion',views.sesion, name= 'sesion'),
    
    path('accounts/profile/',views.profile, name= 'profile'),
    

    path('salir',views.salir, name='salir'),

    path('register', views.crearcuenta, name='crearcuenta'),

    

    path('respuesta/', views.respuesta, name='respuesta'),
    path('contacto/', views.contact, name='contact'),
    path('formulario_Mecanico',views.form_perrito,name="form_perrito"),
    path('vehiculos/', views.listar_vehiculos, name='listar_vehiculos'),
    path('vehiculos/eliminar/<str:patente>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('vehiculos/modificar/<str:patente>/', views.modificar_vehiculo, name='modificar_vehiculo'),


]