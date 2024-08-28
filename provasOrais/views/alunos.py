from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest
from provasOrais.models import Aluno
from provasOrais.forms import AlunoForm


BASE_PATH = 'provasOrais/templates/'
# Create your views here.
def alunos(request: HttpRequest):
    novo = reverse('provas:cadastrarAluno')
    listarAlunos = Aluno.objects.all().filter(ativo=True)
    context={
        'alunos': listarAlunos,
        'novo': novo,
        }
    return render(request, f'{BASE_PATH}listarAlunos.html', context=context)

def aluno(request: HttpRequest, id):
    aluno = get_object_or_404(Aluno, id=id, ativo=True)
    atualizar = reverse('provas:atualizarAluno', args=(id,))
    apagar = reverse('provas:apagarAluno', args=(id,))
    context={
        'listar': {
            'url': reverse('provas:alunos'),
            'nome': 'Alunos',
        },
        'aluno': aluno,
        'atualizar': atualizar,
        'apagar': apagar,
    }
    return render(request, f'{BASE_PATH}consultarAluno.html', context=context)

def cadastrarAluno(request: HttpRequest):
    form_action = reverse('provas:cadastrarAluno')
    if request.method == "POST":
        form = AlunoForm(request.POST)
        context={
            'listar': {
                'url': reverse('provas:alunos'),
                'nome': 'Alunos',
            },
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid:
            aluno = form.save()
            messages.success(request, f'Aluno {aluno.nome} cadastrado com sucesso!')
            return redirect("provas:cadastrarAluno")

        return render(request, f'{BASE_PATH}cadastrarAluno.html', context=context)    
    context={
        'listar': {
            'url': reverse('provas:alunos'),
            'nome': 'Alunos',
        },
        'form': AlunoForm(),
        'form_action': form_action,
    }
    return render(request, f'{BASE_PATH}cadastrarAluno.html', context=context)

def atualizarAluno(request: HttpRequest, id):
    aluno = get_object_or_404(Aluno, id=id, ativo=True)
    form_action = reverse('provas:atualizarAluno', args=(id,))
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        context={
            'listar': {
                'url': reverse('provas:alunos'),
                'nome': 'Alunos',
            },
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid:
            aluno = form.save()
            messages.success(request, f'Aluno {aluno.nome} atualizado com sucesso!')
            return redirect("provas:atualizarAluno", id=aluno.id)

        return render(request, f'{BASE_PATH}cadastrarAluno.html', context=context)
    context={
        'listar': {
            'url': reverse('provas:alunos'),
            'nome': 'Alunos',
        },
        'form': AlunoForm(instance=aluno),
        'form_action': form_action,
    }
    return render(request, f'{BASE_PATH}cadastrarAluno.html', context=context)

def apagarAluno(request: HttpRequest, id):
    aluno = get_object_or_404(Aluno, id=id, ativo=True)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        aluno.delete()
        return redirect('provas:alunos')

    context={
        'listar': {
            'url': reverse('provas:alunos'),
            'nome': 'Alunos',
        },
        'aluno': aluno,
        'confirmation': confirmation,
    }
    return render(request, f'{BASE_PATH}consultarAluno.html', context=context)