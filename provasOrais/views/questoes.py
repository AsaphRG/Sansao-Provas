from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest
from provasOrais.forms import QuestaoForm
from provasOrais.models import Questao

BASE_PATH = 'provasOrais/templates/'
# Create your views here.
def questoes(request):
    novo = reverse('provas:cadastrarQuestao')
    listarQuestoes = Questao.objects.all().filter(ativo=True)
    context={
        'questoes': listarQuestoes,
        'novo': novo,
    }
    return render(request, f'{BASE_PATH}listarQuestoes.html', context=context)

def questao(request, id):
    questao = get_object_or_404(Questao, id=id, ativo=True)
    context={
        'listar': {
            'url': reverse('provas:questoes'),
            'nome': 'Questões',
        },
        'atualizar': reverse('provas:atualizarQuestao', args=(id,)),
        'apagar': reverse('provas:apagarQuestao', args=(id,)),
        'questao': questao,
    }
    return render(request, f'{BASE_PATH}consultarQuestao.html', context=context)

def cadastrarQuestao(request: HttpRequest):
    if request.method == "POST":
        form = QuestaoForm(request.POST)
        context={
            'listar': {
                'url': reverse('provas:questoes'),
                'nome': 'Questões',
            },
            'form': form,
        }

        if form.is_valid:
            questao = form.save()
            messages.success(request, f'Questão {questao.id} cadastrada com sucesso!')
            return redirect("provas:cadastrarQuestao")

        return render(request, f'{BASE_PATH}cadastrarQuestao.html', context=context)    
    context={
        'listar': {
            'url': reverse('provas:questoes'),
            'nome': 'Questões',
        },
        'form': QuestaoForm(),
    }
    return render(request, f'{BASE_PATH}cadastrarQuestao.html', context=context)

def atualizarQuestao(request: HttpRequest, id):
    questao = get_object_or_404(Questao, id=id, ativo=True)
    form_action = reverse('provas:atualizarQuestao', args=(id,))
    if request.method == "POST":
        form = QuestaoForm(request.POST, instance=questao)
        context={
            'listar': {
                'url': reverse('provas:questoes'),
                'nome': 'Questões',
            },
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid:
            questao = form.save()
            messages.success(request, f'Questão {questao.id} atualizada com sucesso!')
            return redirect('provas:atualizarQuestao', id=questao.id)

        return render(request, f'{BASE_PATH}cadastrarQuestao.html', context=context)    
    context={
        'listar': {
            'url': reverse('provas:questoes'),
            'nome': 'Questões',
        },
        'form': QuestaoForm(instance=questao),
        'form_action': form_action,
    }
    return render(request, f'{BASE_PATH}cadastrarQuestao.html', context=context)

def apagarQuestao(request: HttpRequest, id):
    questao = get_object_or_404(Questao, id=id, ativo=True)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        questao.delete()
        return redirect('provas:questoes')

    context={
        'listar': {
            'url': reverse('provas:questoes'),
            'nome': 'Questões',
        },
        'questao': questao,
        'confirmation': confirmation,
    }
    return render(request, f'{BASE_PATH}consultarQuestao.html', context=context)