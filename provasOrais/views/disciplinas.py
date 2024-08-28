from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest
from provasOrais.forms import DisciplinaForm
from provasOrais.models import Disciplina


BASE_PATH = 'provasOrais/templates/'
# Create your views here.
def disciplinas(request):
    novo = reverse('provas:cadastrarDisciplina')
    listarDisciplina = Disciplina.objects.all().filter(ativo=True)
    context={
        'disciplinas': listarDisciplina,
        'novo': novo,
    }
    return render(request, f'{BASE_PATH}listarDisciplinas.html', context=context)

def disciplina(request, id):
    disciplina = get_object_or_404(Disciplina, id=id, ativo=True)
    atualizar = reverse('provas:atualizarDisciplina', args=(id,))
    apagar = reverse('provas:apagarDisciplina', args=(id,))
    context={
        'listar': {
            'url': reverse('provas:disciplinas'),
            'nome': 'Disciplinas',
        },
        'disciplina': disciplina,
        'atualizar': atualizar,
        'apagar': apagar,
    }
    return render(request, f'{BASE_PATH}consultarDisciplina.html', context=context)

def cadastrarDisciplina(request: HttpRequest):
    form_action = reverse('provas:cadastrarDisciplina')
    if request.method == "POST":
        form = DisciplinaForm(request.POST)
        context={
        'listar': {
            'url': reverse('provas:disciplinas'),
            'nome': 'Disciplinas',
        },
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid:
            disciplina = form.save()
            messages.success(request, f'Disciplina {disciplina.disciplina} cadastrada com sucesso!')
            return redirect("provas:cadastrarDisciplina")

        return render(request, f'{BASE_PATH}cadastrarDisciplina.html', context=context)
    context={
        'listar': {
            'url': reverse('provas:disciplinas'),
            'nome': 'Disciplinas',
        },
        'form': DisciplinaForm(),
        'form_action': form_action,
    }
    return render(request, f'{BASE_PATH}cadastrarDisciplina.html', context=context)

def atualizarDisciplina(request: HttpRequest, id):
    disciplina = get_object_or_404(Disciplina, id=id, ativo=True)
    form_action = reverse('provas:atualizarDisciplina', args=(id,))
    if request.method == "POST":
        form = DisciplinaForm(request.POST, instance=disciplina)
        context={
            'listar': {
                'url': reverse('provas:disciplinas'),
                'nome': 'Disciplinas',
            },
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid:
            disciplina = form.save()
            messages.success(request, f'Disciplina {disciplina.disciplina} alterada com sucesso!')
            return redirect("provas:atualizarDisciplina", id=disciplina.id)

        return render(request, f'{BASE_PATH}cadastrarDisciplina.html', context=context)
    context={
        'listar': {
            'url': reverse('provas:disciplinas'),
            'nome': 'Disciplinas',
        },
        'form': DisciplinaForm(instance=disciplina),
        'form_action': form_action,
    }
    return render(request, f'{BASE_PATH}cadastrarDisciplina.html', context=context)

def apagarDisciplina(request: HttpRequest, id):
    disciplina = get_object_or_404(Disciplina, id=id, ativo=True)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        disciplina.delete()
        return redirect('provas:disciplinas')

    context={
        'listar': {
            'url': reverse('provas:disciplinas'),
            'nome': 'Disciplinas',
        },
        'disciplina': disciplina,
        'confirmation': confirmation,
    }
    return render(request, f'{BASE_PATH}consultarDisciplina.html', context=context)