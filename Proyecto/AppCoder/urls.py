from django.urls import path
from django.contrib.auth.views import LogoutView
from AppCoder.views import Inicio, CelularPage, ComputadoraPage, ConsolaPage, ConsolaDetalle, CelularDetalle, ComputadoraDetalle, ConsolaEditar, CelularEditar, ComputadoraEditar, ConsolaDelete, ComputadoraDelete, CelularDelete, ComentarioPage, LoginPage, RegistroPage, AgregarProducto, SobreMi

urlpatterns = [
    # Menu y inicio
    path('inicio/', Inicio.as_view(), name="inicio"),
    # Login y registro de usuarios
    path('login/', LoginPage.as_view(), name="login"),
    path('registro/', RegistroPage.as_view(), name="registro"),
    path('logout/', LogoutView.as_view(next_page='inicio'), name="logout"),
    # Sección sobre mi
    path('sobreMi/', SobreMi, name="sobreMi"),
    # Crear nuevos productos
    path('agregarProducto/', AgregarProducto.as_view(), name="agregarProducto"),
    # Lista de los productos
    path('listaCelulares/', CelularPage.as_view(), name="listaCelulares"),
    path('listaComputadoras/', ComputadoraPage.as_view(), name="listaComputadoras"),
    path('listaConsolas/', ConsolaPage.as_view(), name="listaConsolas"),
    # Detalles de los productos
    path('detalleCelular/<int:pk>/', CelularDetalle.as_view(), name="celular"),
    path('detalleComputadora/<int:pk>/', ComputadoraDetalle.as_view(), name="computadora"),
    path('detalleConsola/<int:pk>/', ConsolaDetalle.as_view(), name="consola"),
    # Comentarios de los productos
    path('detalleConsola/<int:pk>/comentario/', ComentarioPage.as_view(), name="comentario_consola"),
    path('detalleCelular/<int:pk>/comentario/', ComentarioPage.as_view(), name="comentario_celular"),
    path('detalleComputadora/<int:pk>/comentario/', ComentarioPage.as_view(), name="comentario_computadora"),
    # Editar los productos
    path('editarConsola/<int:pk>/', ConsolaEditar.as_view(), name="editarConsola"),
    path('editarCelular/<int:pk>/', CelularEditar.as_view(), name="editarCelular"),
    path('editarComputadora/<int:pk>/', ComputadoraEditar.as_view(), name="editarComputadora"),
    # Borrar los productos
    path('borradoConsola/<int:pk>/', ConsolaDelete.as_view(), name="borrarConsola"),
    path('borradoCelular/<int:pk>/', CelularDelete.as_view(), name="borrarCelular"),
    path('borradoComputadora/<int:pk>/', ComputadoraDelete.as_view(), name="borrarComputadora")
]