from django.contrib.auth.models import User
from django.shortcuts import  render,redirect,get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views import View
from django.contrib import messages



def index(request):
    return render(request, 'index.html')

class PessoaListView(ListView):
    model = Pessoa
    template_name = "pessoa_list.html"

class PessoaCreateView(CreateView):
    model = Pessoa
    fields = '__all__'
    template_name = "form.html"
    success_url = reverse_lazy('pessoa-list')

class PessoaUpdateView(UpdateView):
    model = Pessoa
    fields = '__all__'
    template_name = "form.html"
    success_url = reverse_lazy('pessoa-list')

class PessoaDeleteView(DeleteView):
    model = Pessoa
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('pessoa-list')


# Aula
class AulaListView(ListView):
    model = Aula
    template_name = "aula_list.html"

class AulaCreateView(CreateView):
    model = Aula
    fields = '__all__'
    template_name = "form.html"
    success_url = reverse_lazy('aula-list')

class AulaUpdateView(UpdateView):
    model = Aula
    fields = '__all__'
    template_name = "form.html"
    success_url = reverse_lazy('aula-list')

class AulaDeleteView(DeleteView):
    model = Aula
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('aula-list')


# Jogo
class JogoListView(ListView):
    model = Jogo
    template_name = "jogo_list.html"

class JogoCreateView(CreateView):
    model = Jogo
    fields = '__all__'
    template_name = "form.html"
    success_url = reverse_lazy('jogo-list')

class JogoUpdateView(UpdateView):
    model = Jogo
    fields = '__all__'
    template_name = "form.html"
    success_url = reverse_lazy('jogo-list')

class JogoDeleteView(DeleteView):
    model = Jogo
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('jogo-list')


# Comentário
class ComentarioListView(ListView):
    model = Comentario
    template_name = "comentario_list.html"

class ComentarioCreateView(CreateView):
    model = Comentario
    fields = '__all__'
    template_name = "form.html"
    success_url = reverse_lazy('comentario-list')


class RegistroView(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'registro.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object

        Pessoa.objects.create(
            nome=form.cleaned_data['nome'],
            email=user.email,
            data_nasc=form.cleaned_data.get('data_nasc'),  # agora pode ser opcional
            cidade=form.cleaned_data['cidade'],
            perfil=form.cleaned_data.get('perfil'),  # também pode ser opcional
            cpf=form.cleaned_data.get['cpf']
        )
        return response
    
# def jogo_memoria(request):
#     return render(request, 'jogo_memoria.html')

