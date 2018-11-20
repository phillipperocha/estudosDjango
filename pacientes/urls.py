"""primeiro_projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from .views import pacientes_listar, paciente_criar, paciente_atualizar, paciente_deletar

#Quando alguém digitar /pacientes vai vir pra cá
urlpatterns = [
    # Quando chamar /pacientes/listar vai executar a função pacientes_listar da VIEWS
    path('listar/', pacientes_listar, name="pacientes_listar"),

    path('criar/', paciente_criar, name="paciente_criar"), # Podemos dar apeldios para as URLS

    # Precisaremos entrar com o ID para identificar o usuário que será atualizado
    path('atualizar/<int:id>/', paciente_atualizar, name="paciente_atualizar"),

    path('deletar/<int:id>/', paciente_deletar, name="paciente_deletar"),
]
