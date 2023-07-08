from django.urls import path
from .views import inicio,index, form_perrito, form_mod_vehiculo, form_del_vehiculo, form_contacto ,nosotros, perros, crud, salir, sesion, crearcuenta, contact, respuesta, aceite, bujias, pastillas


urlpatterns = [
    path('',index,name="index"),
   
    path('inicio',inicio,name="inicio"),
    
    path('Nosotros',nosotros,name='nosotros'),

    path('aceite',aceite,name='aceite'),

    path('bujias',bujias,name='bujias'),

    path('pastillas',pastillas,name='pastillas'),

    path('Atenciones',crud,name="crud"),

    path('Misión',perros,name='perros'),

    path('sesion',sesion, name= 'sesion'),

    path('salir', salir, name='salir'),

    path("register", crearcuenta, name="crearcuenta"),

    path('respuesta/', respuesta, name='respuesta'),
    path('contacto/', contact, name='contact'),
    path('formulario_Mecanico',form_perrito,name="form_perrito"),
    path('form-mod-vehiculo/<id>',form_mod_vehiculo,name="form_mod_vehiculo"),
    path('form-del-vehiculo/<id>',form_del_vehiculo,name="form_del_vehiculo"),
]