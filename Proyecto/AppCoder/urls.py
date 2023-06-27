from django.urls import path
from AppCoder.views import Inicio, CelularPage, ComputadoraPage, ConsolaPage, ConsolaDetalle, CelularDetalle, ComputadoraDetalle, ConsolaDelete, ComputadoraDelete, CelularDelete, ComentarioPage, LoginPage, RegistroPage, AgregarProducto

urlpatterns = [
    path('inicio/', Inicio.as_view(), name="Inicio"),
    path('listaCelulares/', CelularPage.as_view(), name="ListaCelulares"),
    path('listaComputadoras/', ComputadoraPage.as_view(), name="ListaComputadoras"),
    path('listaConsolas/', ConsolaPage.as_view(), name="ListaConsolas"),
    path('detalleCelular/<int:pk>/', CelularDetalle.as_view(), name="Celular"),
    path('listaComputadoras/<int:pk>/', ComputadoraDetalle.as_view(), name="Computadora"),
    path('listaConsolas/<int:pk>/', ConsolaDetalle.as_view(), name="Consola"),
    path('detalleConsola/<int:pk>/comentario/', ComentarioPage.as_view(), name="comentario"),
    path('detalleCelular/<int:pk>/comentario/', ComentarioPage.as_view(), name="comentario"),
    path('detalleComputadora/<int:pk>/comentario/', ComentarioPage.as_view(), name="comentario"),
    path('borradoConsola/<int:pk>/', ConsolaDelete.as_view(), name="BorrarConsola"),
    path('borradoCelular/<int:pk>/', CelularDelete.as_view(), name="BorrarCelular"),
    path('borradoComputadora/<int:pk>/', ComputadoraDelete.as_view(), name="BorrarComputadora"),
    path('login/', LoginPage.as_view(), name="Login"),
    path('registro/', RegistroPage.as_view(), name="Registro"),
    path('agregarProducto/', AgregarProducto.as_view(), name="AgregarProducto")
]