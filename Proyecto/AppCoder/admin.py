from django.contrib import admin
from .models import Producto, Comentario, Usuario

admin.site.register(Producto)

admin.site.register(Comentario)

admin.site.register(Usuario)