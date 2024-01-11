from django.shortcuts import render
from .models import Usuario

# Create your views here.


def home(request):
    return render(request, 'usuarios/home.html')


def usuarios(request):

    # Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.name = request.POST.get('name')
    novo_usuario.sobrenome = request.POST.get('sobrenome')
    novo_usuario.nascimento = request.POST.get('nascimento')
    novo_usuario.phone = request.POST.get('phone')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.save()

    # Exibir todos os usuários já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)
