from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from requests import request
from django.contrib.auth.models import User

# Create your models here.
class Ciudad(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        	return self.nombre
	

class Usuario(AbstractUser):
    # atributos adicionales.
    email = models.EmailField('email address', unique = True)
    ciudad = models.ForeignKey(to=Ciudad ,on_delete=models.CASCADE, default=1)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'ciudad']


class Idioma(models.Model):
	nombre = models.CharField(max_length=255)

	def __str__(self):
        	return self.nombre


class Genero(models.Model):
	nombre = models.CharField(max_length=255)
	
	def __str__(self):
        	return self.nombre

class Editorial(models.Model):
	nombre = models.CharField(max_length=255)

	def __str__(self):
        	return self.nombre

	
class Tipo(models.Model):
	nombre = models.CharField(max_length=255)

	def __str__(self):
        	return self.nombre


class Articulo(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    stock = models.IntegerField()
    genero = models.ManyToManyField(Genero)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True)
    presencial = models.BooleanField(default=False,null=True, blank=True)

	
    def __str__(self):
        return self.nombre
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        
class Compra(models.Model):
	fecha = models.DateField()
	precio_total = models.IntegerField()
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
class Ejemplar(models.Model):
	articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)

class Orden(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)
    transaccion_id = models.CharField(max_length=100, null=True)
    objects = models.Manager()


    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        ordenitems = OrdenItem.objects.all()
        for i in ordenitems:
            if i.producto.presencial == False:
                shipping = True
            return shipping
   

    @property
    def get_cart_total(self):
        ordenitems = OrdenItem.objects.all()
        total = sum([item.get_total for item in ordenitems])
        return total 

    @property
    def get_cart_items(self):
        ordenitems = OrdenItem.objects.all()
        total = sum([item.cantidad for item in ordenitems])
        return total 

class OrdenItem(models.Model):
    producto = models.ForeignKey(Articulo, on_delete=models.SET_NULL, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha_anadido = models.DateTimeField(auto_now_add=True)

    @property  
    def get_total(self):
        total = self.producto.precio * self.cantidad
        return total

class DireccionEntrega(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True)
    direccion = models.CharField(max_length=200, null=False)
    ciudad = models.CharField(max_length=200, null=False)
    region = models.CharField(max_length=200, null=False)
    codigo_postal = models.CharField(max_length=200, null=False)
    fecha_anadido = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(null=True)

    def __str__(self):
	    return self.direccion