from django.urls import path
from AppCoder.views import inicio, listaCelulares, listaComputadoras, listaConsolas, listaOtros, login, registro

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('listaCelulares/', listaCelulares, name="ListaCelulares"),
    path('listaComputadoras/', listaComputadoras, name="ListaComputadoras"),
    path('listaConsolas/', listaConsolas, name="ListaConsolas"),
    path('listaOtros/', listaOtros, name="ListaOtros"),
    path('login/', login, name="Login"),
    path('registro/', registro, name="Registro")
]