from django.urls import path
from . import views

urlpatterns = [
    # ALUNOS
    path('alunos/', views.listar_alunos, name='listar_alunos'),
    path('alunos/novo/', views.adicionar_aluno, name='adicionar_aluno'),
    path('alunos/editar/<int:id>/', views.editar_aluno, name='editar_aluno'),
    path('alunos/excluir/<int:id>/', views.excluir_aluno, name='excluir_aluno'),

    # FREQUÊNCIA
    path('frequencias/', views.listar_frequencias, name='listar_frequencias'),
    path('frequencias/novo/', views.adicionar_frequencia, name='adicionar_frequencia'),
    path('frequencias/editar/<int:id>/', views.editar_frequencia, name='editar_frequencia'),
    path('frequencias/excluir/<int:id>/', views.excluir_frequencia, name='excluir_frequencia'),
]
