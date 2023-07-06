from django.shortcuts import render, redirect
from  .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
from django.db.models import Q
import requests

def comprar(request):
    carro = request.session.get("carro", [])
    total = 0
    for item in carro:
        total += item[5]
    venta = Venta()
    venta.cliente = request.user
    venta.total = total
    venta.save()
    for item in carro:
        producto = Producto.objects.get(codigo=item[0])
        detalle = DetalleVenta()
        detalle.producto = Producto.objects.get(codigo = item[0])
        detalle.precio = item[3]
        detalle.cantidad = item[4]
        detalle.venta = venta
        detalle.save()
        producto.stock = producto.stock - item[4]
        producto.save()
        request.session["carro"] = []
    return redirect(to="carrito")
    


def dropitem(request, codigo):
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            if item[4] > 1:
                item[4] -= 1
                item[5] = item[3] * item[4]
                break
            else:
                carro.remove(item)
    request.session["carro"] = carro
    return redirect(to="carrito")

def addtocar(request, codigo):
    producto = Producto.objects.get(codigo = codigo)
    carro = request.session.get("carro", [])
    for item in carro:
        if producto.oferta:
            if item[0] == codigo:
                item[4] += 1
                item[5] = round((item[3]) * item[4])
                break
        else:
            if item[0] == codigo:
                item[4] += 1
                item[5] = item[3] * item[4]
                break
    else:
        if producto.oferta:
            carro.append([codigo, producto.nombre,producto.imagen, round(producto.precio * 0.8), 1, round(producto.precio * 0.8)])
        else:
            carro.append([codigo, producto.nombre,producto.imagen, producto.precio, 1, producto.precio])
    request.session["carro"] = carro
    return redirect(to="home")
def addtocar2(request, codigo):
    producto = Producto.objects.get(codigo = codigo)
    carro = request.session.get("carro", [])
    for item in carro:
        if producto.oferta:
            if item[0] == codigo:
                item[4] += 1
                item[5] = round((item[3]) * item[4])
                break
        else:
            if item[0] == codigo:
                item[4] += 1
                item[5] = item[3] * item[4]
                break
    else:
        if producto.oferta:
            carro.append([codigo, producto.nombre,producto.imagen, round(producto.precio * 0.8), 1, round(producto.precio * 0.8)])
        else:
            carro.append([codigo, producto.nombre,producto.imagen, producto.precio, 1, producto.precio])
    request.session["carro"] = carro
    return redirect(to="productos")
def home(request):   
    carrusel = Producto.objects.filter(Q(codigo="006") | Q(codigo="007") | Q(codigo="008"))
    cajaprod = Producto.objects.filter(Q(codigo="001") | Q(codigo="002") | Q(codigo="003")| Q(codigo="004")| Q(codigo="005"))
    context2 = {'carrusel':carrusel,'cajaprod':cajaprod}
    if request.session.get("modificado", None):
        context2["modificado"] = True
        del request.session["modificado"]
    suscrito(request, context2)
    return render(request,'core/index.html',context2)
def suscribir(request):
    context = {}

    if request.method == "POST":
        if request.user.is_authenticated:
            resp = requests.get(f"http://127.0.0.1:8000/api/suscribir/{request.user.email}")
            context["mensaje"] = resp.json()["mensaje"]
            suscrito(request, context)
        return render(request, 'core/suscripcion.html', context)
    else:
        suscrito(request, context)
        return render(request, 'core/suscripcion.html', context)
def suscrito(request, context):
    if request.user.is_authenticated:
        email = request.user.email
        resp = requests.get(f"http://127.0.0.1:8000/api/suscrito/{email}")
        context["suscrito"] = resp.json()["suscrito"]
def carrito(request):
    context = {}
    carro = request.session.get("carro", [])
    suscrito(request, context)
    context["carro"] = carro
    return render(request, 'core/carrito.html', context)
def limpiar(request):
    request.session.flush()
    return redirect(to="carrito")

def crudprod(request):
    return render(request,'core/crudProd.html')
def cuentaAdmin(request):
    return render(request, 'core/cuentaAdmin.html')
def login(request):
    return render(request,'core/login.html')
def perfil(request):
    context = {}
    suscrito(request, context)
    ventas = Venta.objects.filter(cliente = request.user)
    context["ventas"] = ventas
    return render(request,'core/perfil.html', context)
def productos(request):
    context = {}
    productos = Producto.objects.all()
    suscrito(request, context)
    context["productos"] = productos
    return render(request,'core/productos.html', context)
def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
    else:
        registro = Registro()
    return render(request,'core/registro.html',{'form':registro})
def detalle(request, codigo):
    detalleventa = DetalleVenta.objects.filter(venta = codigo)
    return render(request, 'core/detalle.html', {'detalleventa':detalleventa})
def logout(request):
    return logout_then_login(request, login_url="login")

