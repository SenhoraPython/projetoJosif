"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  include,path
from app.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('registrar/', RegistroView.as_view(), name='registro'),


    path('pessoas/', PessoaListView.as_view(), name='pessoa-list'),
    path('pessoas/novo/', PessoaCreateView.as_view(), name='pessoa-create'),
    path('pessoas/<int:pk>/editar/', PessoaUpdateView.as_view(), name='pessoa-update'),
    path('pessoas/<int:pk>/excluir/', PessoaDeleteView.as_view(), name='pessoa-delete'),

    path('aulas/', AulaListView.as_view(), name='aula-list'),
    path('aulas/nova/', AulaCreateView.as_view(), name='aula-create'),
    path('aulas/<int:pk>/editar/', AulaUpdateView.as_view(), name='aula-update'),
    path('aulas/<int:pk>/excluir/', AulaDeleteView.as_view(), name='aula-delete'),

    path('jogos/', JogoListView.as_view(), name='jogo-list'),
    path('jogos/novo/', JogoCreateView.as_view(), name='jogo-create'),
    path('jogos/<int:pk>/editar/', JogoUpdateView.as_view(), name='jogo-update'),
    path('jogos/<int:pk>/excluir/', JogoDeleteView.as_view(), name='jogo-delete'),

    path('comentarios/', ComentarioListView.as_view(), name='comentario-list'),
    path('comentarios/novo/', ComentarioCreateView.as_view(), name='comentario-create'),

    #path('contribua/', views.contribua, name='contribua'),
    path('jogo/', TemplateView.as_view(template_name='jogo_memoria.html'), name='jogo-memoria')
    
]
