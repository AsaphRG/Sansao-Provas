from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User


# Create your models here.
class Disciplina(models.Model):
    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
    
    disciplina = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True)
    # owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self) -> str:
        return self.disciplina


class Assunto(models.Model):
    class Meta:
        verbose_name = 'Assunto'
        verbose_name_plural = 'Assuntos'
    
    assunto = models.CharField(max_length=255)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True)
    # owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self) -> str:
        return self.assunto


class Turma(models.Model):
    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
    
    Turnos = models.TextChoices('Turnos', 'Diurno Matutino Vespertino Noturno')

    numero = models.CharField(max_length=255)
    turno = models.CharField(choices=Turnos, default='Diurno', max_length=255)
    ano = models.CharField(max_length=4)
    created_date = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True)
    # owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True)
    
    def __str__(self) -> str:
        return self.numero


class Questao(models.Model):
    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'

    questao = models.TextField()
    assunto = models.ForeignKey(Assunto, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True)
    # owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self) -> str:
        return self.questao


class Aluno(models.Model):
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    nome = models.CharField(max_length=255)
    turma = models.ForeignKey(Turma, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True)
    # owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self) -> str:
        return self.nome


class Prova(models.Model):
    class Meta:
        verbose_name = 'Prova'
        verbose_name_plural = 'Provas'

    aluno = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING)
    nota = models.FloatField(max_length=10, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True)


class Pergunta(models.Model):
    class Meta:
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'

    prova = models.ForeignKey(Prova, on_delete=models.DO_NOTHING)
    questao = models.ForeignKey(Questao, on_delete=models.DO_NOTHING)
    resposta = models.TextField(blank=True)
    nota = models.FloatField(max_length=10, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True)
    # owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self) -> str:
        return f'{self.questao}:\n{self.resposta}'
