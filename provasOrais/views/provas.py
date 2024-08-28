from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest
from provasOrais.forms import nonModelProvaForm, PerguntaForm, AtualizarPerguntaForm
from provasOrais.models import Prova, Pergunta, Questao, Aluno
from random import choices
from utils.misc import round_for_half

BASE_PATH = 'provasOrais/templates/'


# Listar itens

def provas(request: HttpRequest):
    context = {
        'novo': reverse('provas:cadastrarProva'),
        'provas': Prova.objects.filter(ativo=True),
    }
    return render(request, f'{BASE_PATH}listarProvas.html', context=context)


# Consultar 1 item

def prova(request: HttpRequest, id):
    context={
        'listar': {
            'url': reverse('provas:provas'),
            'nome': 'Provas',
        },
        'atualizar': reverse('provas:atualizarProva', args=(id,)),
        'apagar': reverse('provas:apagarProva', args=(id,)),
        'prova': get_object_or_404(Prova, id=id, ativo=True),
        'perguntas': Pergunta.objects.filter(prova=id, ativo=True),
    }
    return render(request, f'{BASE_PATH}consultarProva.html', context=context)

# Dados para cadastrar prova

def dadosProva(request: HttpRequest):
    return render(request, f'{BASE_PATH}cadastrarProva.html')

# Cadastrar novo item

def cadastrarProva(request: HttpRequest):
    form_action = reverse('provas:cadastrarProva')
    context={
        'listar': {
            'url': reverse('provas:provas'),
            'nome': 'Provas',
        },
        'form': nonModelProvaForm(),
        'form_action': form_action,
    }

    if request.method == 'POST' and request.POST.__contains__('assunto'):
        assunto = request.POST['assunto'][0]
        questoesDB = list(Questao.objects.filter(assunto=assunto))
        questoes = choices(questoesDB, k = 3)
        questoesForm = []
        for questao in questoes:
            questoesForm.append(PerguntaForm(questao))
        context={
            'form': PerguntaForm(),
            'questoes': questoes,
            'aluno': request.POST['aluno'],
            'form_action': form_action,
        }
        return render(request, f'{BASE_PATH}cadastrarProva.html', context=context)
    
    if request.method == "POST" and request.POST.__contains__('questao'):
        questoes = request.POST.getlist('questao')
        respostas = request.POST.getlist('resposta')
        notas = request.POST.getlist('nota')

        aluno = Aluno.objects.filter(id=request.POST['aluno'])[0]

        perguntas = [Questao.objects.filter(id=questao)[0] for questao in questoes]

        notaProva = 0.0
        for valor in notas:
            try:
                valor = float(valor)
                notaProva += valor
            except:
                pass
        notaProva /= len(notas)
        notaProva = round_for_half(notaProva)

        prova = Prova(aluno=aluno, nota=notaProva)
        prova.save()

        for count in range(len(questoes)):
            pergunta = Pergunta(prova=prova, questao=perguntas[count], resposta=respostas[count], nota=notas[count])
            pergunta.save()
            
        messages.success(request, f'Prova {prova.id} do aluno {aluno} foi cadastrada com sucesso e a nota é {notaProva}')
    
    return render(request, f'{BASE_PATH}cadastrarProva.html', context=context)


# Atualizar item

def atualizarProva(request: HttpRequest, id):
    form_action = reverse('provas:atualizarProva', args=(id,))
    prova = get_object_or_404(Prova, id=id, ativo=True)
    perguntas = Pergunta.objects.filter(prova=id)
    forms = []
    for pergunta in perguntas:
        # pergunta.questao = Questao.objects.filter(id=pergunta.questao.id)[0]
        perguntaForm = AtualizarPerguntaForm(instance=pergunta)
        perguntaForm.questao = pergunta.questao
        forms.append(perguntaForm)
    context={
        'listar': {
            'url': reverse('provas:provas'),
            'nome': 'Provas',
        },
        'atualizar': reverse('provas:atualizarProva', args=(id,)),
        'apagar': reverse('provas:apagarProva', args=(id,)),
        'prova': prova,
        'perguntas': perguntas,
        'form': forms,
        'form_action': form_action,
    }

    if request.method == 'POST':
        questoes = request.POST.getlist('questao')
        respostas = request.POST.getlist('resposta')
        notas = request.POST.getlist('nota')

        notaProva = 0.0
        for valor in notas:
            try:
                valor = float(valor)
                notaProva += valor
            except:
                pass
        notaProva /= len(notas)
        notaProva = round_for_half(notaProva)
        prova.nota = notaProva
        prova.save()

        for count in range(len(questoes)):
            pergunta = get_object_or_404(Pergunta, id=perguntas[count].id)
            pergunta.resposta = respostas[count]
            pergunta.nota = notas[count]
            print(pergunta)
            pergunta.save()

        messages.success(request, f'Prova {prova.id} atualizada com sucesso!')
        return redirect('provas:prova', id=id)

    return render(request, f'{BASE_PATH}atualizarProva.html', context=context)


# Apagar item

def apagarProva(request: HttpRequest, id):
    prova = get_object_or_404(Prova, id=id, ativo=True)
    perguntas = Pergunta.objects.filter(prova=id, ativo=True)
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        prova.ativo = False
        prova.save()
        for pergunta in perguntas:
            pergunta.ativo = False
            pergunta.save()
        return redirect('provas:provas')

    context={
        'listar': {
            'url': reverse('provas:provas'),
            'nome': 'Provas',
        },
        'atualizar': reverse('provas:atualizarProva', args=(id,)),
        'apagar': reverse('provas:apagarProva', args=(id,)),
        'prova': get_object_or_404(Prova, id=id, ativo=True),
        'perguntas': Pergunta.objects.filter(prova=id, ativo=True),
        'confirmation': confirmation,
    }

    return render(request, f'{BASE_PATH}consultarProva.html', context=context)
