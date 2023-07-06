from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
class Producto(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    oferta = models.BooleanField()
    imagen = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200, default = 'producto')
    
    def tachado(self):
        antiguo = self.precio
        if self.oferta:
            self.precio = round(self.precio * 0.8)
            return "$"+str(round(int(antiguo)))
    def suscrito(self, Suscripcion):
        if Suscripcion.estado:
            round(self.precio * 0.95)
            return "$"+str(round(int(self.precio)))
        return ""

    def __str__(self):
        return self.nombre+"("+self.codigo+")"

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=datetime.now())
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()

    def __str__(self):
        return str(self.id)+" "+self.cliente.username+" "+str(self.fecha)

class DetalleVenta(models.Model):
    id=models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return str(self.id)+" "+self.producto.nombre[0:25]+" "+ str(self.venta.id)
    
