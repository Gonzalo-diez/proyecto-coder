from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    autor = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatares/")

    def __str__(self):
        return self.autor.username

class Producto(models.Model):
    productoSeleccion = (
        ('celular', 'Celular'),
        ('computadora', 'Computadora'),
        ('consola', 'Consola')
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    producto = models.CharField(max_length=15, choices=productoSeleccion, default='celular')
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)   
    year = models.IntegerField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    telefonoContacto = models.IntegerField()
    emailContacto = models.EmailField()
    imagenProducto = models.ImageField(null=True, blank=True, upload_to="images/")

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    comentario = models.ForeignKey(Producto, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje  = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
         ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)