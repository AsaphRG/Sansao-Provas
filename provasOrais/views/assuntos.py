from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest
from provasOrais.models import Assunto
from provasOrais.forms import AssuntoForm

BASE_PATH = 'provasOrais/templates/'
# Create your views here.
def assuntos(request):
    listarAssuntos = Assunto.objects.all().filter(ativo=True)
    novo = reverse('provas:cadastrarAssunto')
    context={
        'assuntos': listarAssuntos,
        'novo': novo,
    }
    return render(request, f'{BASE_PATH}listarAssuntos.html', context=context)

def assunto(request, id):
    assunto = Assunto.objects.get(id=id)
    atualizar = reverse('provas:atualizarAssunto', args=(id,))
    apagar = reverse('provas:apagarAssunto', args=(id,))
    context={
        'listar': {
            'url': reverse('provas:assuntos'),
            'nome': 'Assuntos',
        },
        'assunto': assunto,
        'atualizar': atualizar,
        'apagar': apagar,
    }
    return render(request, f'{BASE_PATH}consultarAssunto.html', context=context)

def cadastrarAssunto(request: HttpRequest):
    form_action = reverse('provas:cadastrarAssunto')
    if request.method == "POST":
        form = AssuntoForm(request.POST)
        context={
            'listar': {
                'url': reverse('provas:assuntos'),
                'nome': 'Assuntos',
            },
            'form': form,
            'form': form_action,
        }

        if form.is_valid:
            assunto = form.save()
            messages.success(request, f'Assunto {assunto.assunto} cadastrado com sucesso!')
            return redirect("provas:cadastrarAssunto")

        return render(request, f'{BASE_PATH}cadastrarAssunto.html', context=context)    
    context={
        'listar': {
            'url': reverse('provas:assuntos'),
            'nome': 'Assuntos',
        },
        'form': AssuntoForm(),
        'from_action': form_action,
    }
    return render(request, f'{BASE_PATH}cadastrarAssunto.html', context=context)

def atualizarAssunto(request: HttpRequest, id):
    assunto = get_object_or_404(Assunto, id=id, ativo=True)
    form_action = reverse('provas:atualizarAssunto', args=(id,))
    if request.method == "POST":
        form = AssuntoForm(request.POST, instance=assunto)
        context={
            'listar': {
                'url': reverse('provas:assuntos'),
                'nome': 'Assuntos',
            },
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid:
            assunto = form.save()
            messages.success(request, f'Assunto {assunto.assunto} alterado com sucesso!')
            return redirect("provas:atualizarAssunto", id=assunto.id)

        return render(request, f'{BASE_PATH}cadastrarAssunto.html', context=context)
    context={
        'listar': {
            'url': reverse('provas:assuntos'),
            'nome': 'Assuntos',
        },
        'form': AssuntoForm(instance=assunto),
        'from_action': form_action,
    }
    return render(request, f'{BASE_PATH}cadastrarAssunto.html', context=context)

def apagarAssunto(request: HttpRequest, id):
    assunto = get_object_or_404(Assunto, id=id, ativo=True)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        assunto.delete()
        return redirect('provas:assuntos')

    context={
        'listar': {
            'url': reverse('provas:assuntos'),
            'nome': 'Assuntos',
        },
        'assunto': assunto,
        'confirmation': confirmation,
    }
    return render(request, f'{BASE_PATH}consultarAssunto.html', context=context)
