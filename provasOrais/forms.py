from django import forms
from provasOrais.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


class UsuarioForm(UserCreationForm):
    first_name = forms.CharField(
        required = True,
    )
    last_name = forms.CharField(
        required = True,
    )
    email = forms.EmailField(
        required = True,
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe email com esse nome', code='invalid')
            )
        
        return email


class AlunoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({
            'placeholder': 'Insira seu nome...',
        })

    class Meta:
        model = Aluno
        fields = ('nome', 'turma')


class AssuntoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Assunto
        fields = ('assunto', 'disciplina')


class DisciplinaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Disciplina
        fields = ("disciplina",)


class TurmaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Turma
        fields = ('numero', 'turno', 'ano')


class QuestaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Questao
        fields = ('questao', 'assunto')


class nonModelProvaForm(forms.Form):
    aluno = forms.ModelChoiceField(Aluno.objects.filter(ativo=True))
    assunto = forms.ModelChoiceField(Assunto.objects.filter(ativo=True))


class ProvaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Prova
        fields = ('aluno', 'nota')


class AssuntoPerguntaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Questao
        fields = ('assunto',)


class PerguntaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Pergunta
        fields = ('questao', 'resposta', 'nota')


class AtualizarPerguntaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Pergunta
        fields = ('resposta', 'nota')
