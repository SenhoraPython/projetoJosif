from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Pessoa

class RegistroUsuarioForm(UserCreationForm):
    nome = forms.CharField(label="Nome completo")
    cidade = forms.ModelChoiceField(queryset=Pessoa._meta.get_field('cidade').remote_field.model.objects.all())
    perfil = forms.ModelChoiceField(queryset=Pessoa._meta.get_field('perfil').remote_field.model.objects.all())

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nome', 'cidade', 'perfil']
