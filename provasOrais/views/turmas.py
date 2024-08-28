from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest
from provasOrais.forms import TurmaForm
from provasOrais.models import Turma

BASE_PATH = 'provasOrais/templates/'
# Create your views here.
def turmas(request):
    novo = reverse('provas:cadastrarTurma')
    listarTurmas = Turma.objects.all().filter(ativo=True)
    context={
        'turmas': listarTurmas,
        'novo': novo,
    }
    return render(request, f'{BASE_PATH}listarTurmas.html', context=context)

def turma(request, id):
    turma = get_object_or_404(Turma, id=id, ativo=True)
    atualizar = reverse('provas:atualizarTurma', args=(id,))
    apagar = reverse('provas:apagarTurma', args=(id,))
    context={
        'listar': {
            'url': reverse('provas:turmas'),
            'nome': 'Turmas',
        },
        'turma': turma,
        'atualizar': atualizar,
        'apagar': apagar,
    }
    return render(request, f'{BASE_PATH}consultarTurma.html', context=context)

def cadastrarTurma(request: HttpRequest):
    form_action = reverse('provas:cadastrarTurma')
    if request.method == "POST":
        form = TurmaForm(request.POST)
        context={
            'listar': {
                'url': reverse('provas:turmas'),
                'nome': 'Turmas',
            },
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid:
            turma = form.save()
            messages.success(request, f'Turma {turma.numero} cadastrada com sucesso!')
            return redirect("provas:cadastrarTurma")

        return render(request, f'{BASE_PATH}cadastrarTurma.html', context=context)    
    context={
        'listar': {
            'url': reverse('provas:turmas'),
            'nome': 'Turmas',
        },
        'form': TurmaForm(),
        'form_action': form_action,
    }
    return render(request, f'{BASE_PATH}cadastrarTurma.html', context=context)

def atualizarTurma(request: HttpRequest, id):
    turma = get_object_or_404(Turma, id=id, ativo=True)
    form_action = reverse('provas:atualizarTurma', args=(id,))
    if request.method == "POST":
        form = TurmaForm(request.POST, instance=turma)
        context={
            'listar': {
                'url': reverse('provas:turmas'),
                'nome': 'Turmas',
            },
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid:
            turma = form.save()
            messages.success(request, f'Turma {turma.numero} atualizada com sucesso!')
            return redirect("provas:atualizarTurma")

        return render(request, f'{BASE_PATH}cadastrarTurma.html', context=context)    
    context={
        'listar': {
            'url': reverse('provas:turmas'),
            'nome': 'Turmas',
        },
        'form': TurmaForm(instance=turma),
        'form_action': form_action,
    }
    return render(request, f'{BASE_PATH}cadastrarTurma.html', context=context)

def apagarTurma(request: HttpRequest, id):
    turma = get_object_or_404(Turma, id=id, ativo=True)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        turma.delete()
        return redirect('provas:turmas')

    context={
        'listar': {
            'url': reverse('provas:turmas'),
            'nome': 'Turmas',
        },
        'turma': turma,
        'confirmation': confirmation,
    }
    return render(request, f'{BASE_PATH}consultarTurma.html', context=context)