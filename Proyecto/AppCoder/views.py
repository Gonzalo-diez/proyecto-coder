from django.http import HttpResponse
from django.shortcuts import render
from .models import Tecnologia

def inicio(request): 
    return render(request, "AppCoder/home.html")

def listaCelulares(request):
    return render(request, "AppCoder/listaCelulares.html")

def listaConsolas(request):
    consolas = Tecnologia.objects.all()
    return render(request, "AppCoder/listaConsolas.html", {"consolas": consolas})

def listaComputadoras(request):
    return render(request, "AppCoder/listaComputadoras.html")

def listaOtros(request):
    return render(request, "AppCoder/listaOtros")

def login(request):
    return render(request, "AppCoder/login.html")

def registro(request):
    return render(request, "AppCoder/registro.html")