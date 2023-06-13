from django.urls import path
from AppCoder.views import inicio, listaCelulares, listaComputadoras, listaConsolas, listaOtros, login

urlpatterns = [
    path('', inicio),
    path('listaCelulares/', listaCelulares),
    path('listaComputadoras/', listaComputadoras),
    path('listaConsolas/', listaConsolas),
    path('listaOtros/', listaOtros),
    path('login/', login)
]