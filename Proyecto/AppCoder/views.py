from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from .models import Producto, Comentario
from .forms import FormularioRegistroUsuario, FormularioNuevoProducto, FormularioComentario
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib.auth import login

class Inicio(TemplateView):
    template_name = 'AppCoder/inicio.html'

class RegistroPage(FormView):
    template_name = 'AppCoder/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('Inicio')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('Inicio')
        return super(RegistroPage, self).get(*args, **kwargs)

class LoginPage(LoginView):
    template_name = 'AppCoder/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('Inicio')

    def get_success_url(self):
        return reverse_lazy('Inicio')

class ConsolaPage(LoginRequiredMixin, ListView):
    context_object_name = 'consolas'
    template_name = 'AppCoder/listaConsolas.html'
    login_url = '/login/'

    def get_queryset(self):
        return Producto.objects.filter(producto='consola')


class CelularPage(LoginRequiredMixin, ListView):
    context_object_name = 'celulares'
    template_name = 'AppCoder/listaCelulares.html'
    login_url = '/login/'

    def get_queryset(self):
        return Producto.objects.filter(producto='celular')

class ComputadoraPage(LoginRequiredMixin, ListView):
    context_object_name = 'computadoras'
    template_name = 'AppCoder/listaComputadoras.html'
    login_url = '/login/'

    def get_queryset(self):
        return Producto.objects.filter(producto='computadora')


class ConsolaDetalle(LoginRequiredMixin, DetailView):
    model = Producto
    context_object_name = 'consola'
    template_name = 'AppCoder/detalleConsola.html'

class CelularDetalle(LoginRequiredMixin, DetailView):
    model = Producto
    context_object_name = 'celular'
    template_name = 'AppCoder/detalleCelular.html'

class ComputadoraDetalle(LoginRequiredMixin, DetailView):
    model = Producto
    context_object_name = 'computadora'
    template_name = 'AppCoder/detalleComputadora.html'

class ConsolaEditar(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = FormularioNuevoProducto
    template_name = 'AppCoder/edicionConsola.html'
    success_url = reverse_lazy('Inicio')

class CelularEditar(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = FormularioNuevoProducto
    template_name = 'AppCoder/edicionCelular.html'
    success_url = reverse_lazy('Inicio')

class ComputadoraEditar(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = FormularioNuevoProducto
    template_name = 'AppCoder/edicionComputadora.html'
    success_url = reverse_lazy('Inicio')

class ConsolaDelete(LoginRequiredMixin, DeleteView): 
    model = Producto
    success_url = reverse_lazy('Inicio')
    template_name = 'AppCoder/borradoConsola.html'

class CelularDelete(LoginRequiredMixin, DeleteView): 
    model = Producto
    success_url = reverse_lazy('Inicio')
    template_name = 'AppCoder/borradoCelular.html'

class ComputadoraDelete(LoginRequiredMixin, DeleteView): 
    model = Producto
    success_url = reverse_lazy('Inicio')
    template_name = 'AppCoder/borradoComputadora.html'

class AgregarProducto(LoginRequiredMixin, View):
    form_class = FormularioNuevoProducto
    template_name = 'AppCoder/agregarProducto.html'
    success_url = reverse_lazy('Inicio')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.usuario = request.user
            publicacion.save()
            return redirect(self.success_url)
        else:
            print(form.errors)
        return render(request, self.template_name, {'form': form})

class ComentarioPage(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'AppCoder/comentario.html'
    success_url = reverse_lazy('Inicio')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPage, self).form_valid(form)

def SobreMi(request):
    return render(request, 'AppCoder/sobremi.html')