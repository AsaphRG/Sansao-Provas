from django.urls import path
from provasOrais import views

app_name = 'provas'
urlpatterns = [
    path('', views.home, name='home'),

    path('usuario/novo', views.cadastrarUsuario, name='cadastrarUsuario'),

    path('alunos/', views.alunos, name='alunos'),
    path('alunos/<int:id>/', views.aluno, name='aluno'),
    path('alunos/novo/', views.cadastrarAluno, name='cadastrarAluno'),
    path('alunos/<int:id>/atualizar', views.atualizarAluno, name='atualizarAluno'),
    path('alunos/<int:id>/apagar', views.apagarAluno, name='apagarAluno'),
    
    path('assuntos/', views.assuntos, name='assuntos'),
    path('assuntos/<int:id>/', views.assunto, name='assunto'),
    path('assuntos/novo/', views.cadastrarAssunto, name='cadastrarAssunto'),
    path('assuntos/<int:id>/atualizar', views.atualizarAssunto, name='atualizarAssunto'),
    path('assuntos/<int:id>/apagar', views.apagarAssunto, name='apagarAssunto'),
    
    path('disciplinas/', views.disciplinas, name='disciplinas'),
    path('disciplinas/<int:id>/', views.disciplina, name='disciplina'),
    path('disciplinas/novo/', views.cadastrarDisciplina, name='cadastrarDisciplina'),
    path('disciplinas/<int:id>/atualizar', views.atualizarDisciplina, name='atualizarDisciplina'),
    path('disciplinas/<int:id>/apagar', views.apagarDisciplina, name='apagarDisciplina'),
    
    path('perguntas/', views.perguntas, name='perguntas'),
    path('perguntas/<int:id>/', views.pergunta, name='pergunta'),
    path('perguntas/novo/', views.cadastrarPergunta, name='cadastrarPergunta'),
    path('perguntas/assunto/', views.receberAssunto, name='receberAssunto'),
    path('perguntas/<int:id>/atualizar', views.atualizarPergunta, name='atualizarPergunta'),
    path('perguntas/<int:id>/apagar', views.apagarPergunta, name='apagarPergunta'),
    
    path('questoes/', views.questoes, name='questoes'),
    path('questoes/<int:id>/', views.questao, name='questao'),
    path('questoes/novo/', views.cadastrarQuestao, name='cadastrarQuestao'),
    path('questoes/<int:id>/atualizar', views.atualizarQuestao, name='atualizarQuestao'),
    path('questoes/<int:id>/apagar', views.apagarQuestao, name='apagarQuestao'),
    
    path('turmas/', views.turmas, name='turmas'),
    path('turmas/<int:id>/', views.turma, name='turma'),
    path('turmas/novo/', views.cadastrarTurma, name='cadastrarTurma'),
    path('turmas/<int:id>/atualizar', views.atualizarTurma, name='atualizarTurma'),
    path('turmas/<int:id>/apagar', views.apagarTurma, name='apagarTurma'),

    path('provas/', views.provas, name='provas'),
    path('provas/<int:id>/', views.prova, name='prova'),
    path('provas/novo/pre/', views.dadosProva, name='dadosProva'),
    path('provas/novo/', views.cadastrarProva, name='cadastrarProva'),
    path('provas/<int:id>/atualizar', views.atualizarProva, name='atualizarProva'),
    path('provas/<int:id>/apagar', views.apagarProva, name='apagarProva'),
]
