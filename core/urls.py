from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name='home'),
    path('login', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('cuentaAdmin', cuentaAdmin, name='cuentaAdmin'),
    path('productos', productos, name='productos'),
    path('perfil', perfil, name='perfil'),
    path('registro', registro,name='registro'),
    path('crudProd',crudprod,name='crudProd'),
    path('logout',logout,name='logout'),
    path('addtocar/<codigo>',addtocar,name='addtocar'),
    path('addtocar2/<codigo>',addtocar2,name='addtocar2'),
    path('dropitem/<codigo>',dropitem,name='dropitem'),
    path('carrito',carrito,name='carrito'),
    path('limpiar',limpiar,name='limpiar'),
    path('comprar',comprar,name='comprar'),
    path('detalle/<codigo>',detalle,name='detalle'),
    path('suscribir',suscribir,name='suscribir'),
    
]
