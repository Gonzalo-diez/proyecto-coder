from django.http import HttpResponse
from django.shortcuts import render

def inicio(request): 
    return render(request, "AppCoder/home.html")

def listaCelulares(request):
    return render(request, "AppCoder/listaCelulares.html")

def listaConsolas(request):
    return render(request, "AppCoder/listaConsolas.html")

def listaComputadoras(request):
    return render(request, "AppCoder/listaComputadoras.html")

def listaOtros(request):
    return render(request, "AppCoder/listaOtros")

def login(request):
    return render(request, "AppCoder/login.html")