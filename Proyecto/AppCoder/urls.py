from django.urls import path
from django.contrib.auth.views import LogoutView
from AppCoder.views import Inicio, CelularPage, ComputadoraPage, ConsolaPage, ConsolaDetalle, CelularDetalle, ComputadoraDetalle, ConsolaEditar, CelularEditar, ComputadoraEditar, ConsolaDelete, ComputadoraDelete, CelularDelete, ComentarioPage, LoginPage, RegistroPage, AgregarProducto, SobreMi

urlpatterns = [
    path('inicio/', Inicio.as_view(), name="Inicio"),
    path('login/', LoginPage.as_view(), name="Login"),
    path('registro/', RegistroPage.as_view(), name="Registro"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('sobreMi/', SobreMi, name="SobreMi"),
    path('agregarProducto/', AgregarProducto.as_view(), name="AgregarProducto"),
    path('listaCelulares/', CelularPage.as_view(), name="ListaCelulares"),
    path('listaComputadoras/', ComputadoraPage.as_view(), name="ListaComputadoras"),
    path('listaConsolas/', ConsolaPage.as_view(), name="ListaConsolas"),
    path('detalleCelular/<int:pk>/', CelularDetalle.as_view(), name="Celular"),
    path('listaComputadoras/<int:pk>/', ComputadoraDetalle.as_view(), name="Computadora"),
    path('listaConsolas/<int:pk>/', ConsolaDetalle.as_view(), name="Consola"),
    path('detalleConsola/<int:pk>/comentario/', ComentarioPage.as_view(), name="comentario"),
    path('detalleCelular/<int:pk>/comentario/', ComentarioPage.as_view(), name="comentario"),
    path('detalleComputadora/<int:pk>/comentario/', ComentarioPage.as_view(), name="comentario"),
    path('editarConsola/<int:pk>/', ConsolaEditar.as_view(), name="EditarConsola"),
    path('editarCelular/<int:pk>/', CelularEditar.as_view(), name="EditarCelular"),
    path('editarComputadora/<int:pk>/', ComputadoraEditar.as_view(), name="EditarComputadora"),
    path('borradoConsola/<int:pk>/', ConsolaDelete.as_view(), name="BorrarConsola"),
    path('borradoCelular/<int:pk>/', CelularDelete.as_view(), name="BorrarCelular"),
    path('borradoComputadora/<int:pk>/', ComputadoraDelete.as_view(), name="BorrarComputadora")
]