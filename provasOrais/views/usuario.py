from django.shortcuts import render
from provasOrais.forms import UsuarioForm
from django.http import HttpRequest

BASE_PATH = 'provasOrais/templates/'

def cadastrarUsuario(request: HttpRequest):
    form = UsuarioForm()

    if request.method == "POST":
        form = UsuarioForm(request.POST)

        if form.is_valid():
            form.save()


    context = {
        'form': form
    }

    return render(request, f'{BASE_PATH}cadastrarUsuario.html', context=context)
