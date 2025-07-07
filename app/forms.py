from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cidade, PerfilUsuario

class RegistroUsuarioForm(UserCreationForm):
    nome = forms.CharField(max_length=100)
    data_nasc = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    cidade = forms.ModelChoiceField(queryset=Cidade.objects.all())
    perfil = forms.ModelChoiceField(queryset=PerfilUsuario.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
