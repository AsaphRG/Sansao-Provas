from django.contrib import admin
from provasOrais import models

global_ordering = '-id',
global_max_show_all = 1000
global_list_per_page = 100

# Register your models here.
@admin.register(models.Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = 'id', 'disciplina'
    list_display_links = 'id', 'disciplina'
    search_fields = 'id', 'disciplina'
    ordering = global_ordering
    list_max_show_all = global_max_show_all
    list_per_page = global_list_per_page


@admin.register(models.Assunto)
class AssuntoAdmin(admin.ModelAdmin):
    list_display = 'id', 'assunto', 'disciplina'
    list_display_links = 'id', 'assunto', 'disciplina'
    search_fields = 'id', 'assunto', 'disciplina'
    ordering = global_ordering
    list_max_show_all = global_max_show_all


@admin.register(models.Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = 'id', 'numero', 'turno', 'ano'
    list_display_links = 'id', 'numero', 'turno', 'ano'
    search_fields = 'id', 'numero', 'turno', 'ano'
    ordering = global_ordering
    list_max_show_all = global_max_show_all


@admin.register(models.Questao)
class QuestaoAdmin(admin.ModelAdmin):
    list_display = 'id', 'questao', 'assunto'
    list_display_links = 'id', 'questao', 'assunto'
    search_fields = 'id', 'questao', 'assunto'
    ordering = global_ordering
    list_max_show_all = global_max_show_all


@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'turma'
    list_display_links = 'id', 'nome', 'turma'
    search_fields = 'id', 'nome', 'turma'
    ordering = global_ordering
    list_max_show_all = global_max_show_all


@admin.register(models.Prova)
class ProvaAdmin(admin.ModelAdmin):
    list_display = 'id', 'aluno', 'nota',
    list_display_links = 'id', 'aluno'
    search_fields = 'id', 'aluno', 'nota'
    ordering = global_ordering
    list_max_show_all = global_max_show_all


@admin.register(models.Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = 'id', 'questao', 'resposta', 'nota'
    list_display_links = 'id', 'questao'
    search_fields = 'id', 'questao', 'resposta', 'nota'
    list_editable = 'resposta', 'nota'
    ordering = global_ordering
    list_max_show_all = global_max_show_all
