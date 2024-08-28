from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest
from provasOrais.forms import PerguntaForm, AssuntoPerguntaForm
from provasOrais.models import Pergunta, Questao
from random import choices

BASE_PATH = 'provasOrais/templates/'
# Create your views here.
def perguntas(request):
    novo = reverse('provas:cadastrarPergunta')
    listarPerguntas = Pergunta.objects.all().filter(ativo=True)
    context={
        'perguntas': listarPerguntas,
        'novo': novo,
    }
    return render(request, f'{BASE_PATH}listarPerguntas.html', context=context)

def pergunta(request, id):
    pergunta = get_object_or_404(Pergunta, id=id, ativo=True)
    atualizar = reverse('provas:atualizarPergunta', args=(id,))
    apagar = reverse('provas:apagarPergunta', args=(id,))
    context={
        'listar': {
            'url': reverse('provas:perguntas'),
            'nome': 'Perguntas',
        },
        'pergunta': pergunta,
        'atualizar': atualizar,
        'apagar': apagar,
    }
    return render(request, f'{BASE_PATH}consultarPergunta.html', context=context)

def receberAssunto(request: HttpRequest):
    form = AssuntoPerguntaForm()
    context = {
        'listar': {
            'url': reverse('provas:perguntas'),
            'nome': 'Perguntas',
        },
        'form': form
    }
    return render(request, f'{BASE_PATH}receberAssunto.html', context=context)

def cadastrarPergunta(request: HttpRequest):
    form_action = reverse('provas:cadastrarPergunta')
    if request.method == "POST" and not request.POST.__contains__('assunto'):
        form = PerguntaForm(request.POST)
        
        context={
            'listar': {
                'url': reverse('provas:perguntas'),
                'nome': 'Perguntas',
            },
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid:
            pergunta = form.save()
            messages.success(request, f'Pergunta {pergunta.id} cadastrada com sucesso!')
            return redirect("provas:cadastrarPergunta")

        return render(request, f'{BASE_PATH}cadastrarPergunta.html', context=context)
    if request.method == "POST" and request.POST.__contains__('assunto'):
        assunto = request.POST['assunto'][0]
        questoes = list(Questao.objects.filter(assunto=assunto))
        questao = choices(questoes, k = 3)
        context = {
            'listar': {
                'url': reverse('provas:perguntas'),
                'nome': 'Perguntas',
            },
            'form': PerguntaForm(),
            'questoes': questao,
        }
        return render(request, f'{BASE_PATH}cadastrarPergunta.html', context=context)
    context={
        'listar': {
            'url': reverse('provas:perguntas'),
            'nome': 'Perguntas',
        },
        'form': PerguntaForm(),
        'form_action': form_action,
    }
    return render(request, f'{BASE_PATH}cadastrarPergunta.html', context=context)

def atualizarPergunta(request: HttpRequest, id):
    pergunta = get_object_or_404(Pergunta, id=id, ativo=True)
    form_action = reverse('provas:atualizarPergunta', args=(id,))
    if request.method == "POST":
        form = PerguntaForm(request.POST, instance=pergunta)
        
        context={
            'listar': {
                'url': reverse('provas:perguntas'),
                'nome': 'Perguntas',
            },
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid:
            pergunta = form.save()
            messages.success(request, f'Pergunta {pergunta.id} atualizada com sucesso!')
            return redirect("provas:atualizarPergunta", id=pergunta.id)

        return render(request, f'{BASE_PATH}cadastrarPergunta.html', context=context)
    context={
        'listar': {
            'url': reverse('provas:perguntas'),
            'nome': 'Perguntas',
        },
        'form': PerguntaForm(instance=pergunta),
        'form_action': form_action,
    }
    return render(request, f'{BASE_PATH}cadastrarPergunta.html', context=context)

def apagarPergunta(request: HttpRequest, id):
    pergunta = get_object_or_404(Pergunta, id=id, ativo=True)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        pergunta.delete()
        return redirect('provas:perguntas')

    context={
        'listar': {
            'url': reverse('provas:perguntas'),
            'nome': 'Perguntas',
        },
        'pergunta': pergunta,
        'confirmation': confirmation,
    }
    return render(request, f'{BASE_PATH}consultarPergunta.html', context=context)