from django.shortcuts import render, redirect, get_object_or_404
from .models import aluno, frequencia
from .forms import AlunoForm, FrequenciaForm


# ==========================
# CRUD ALUNO
# ==========================

def listar_alunos(request):
    alunos = aluno.objects.all()
    return render(request, 'frequencia/listar_alunos.html', {'alunos': alunos})


def adicionar_aluno(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_alunos')
    return render(request, 'frequencia/form_aluno.html', {'form': form})


def editar_aluno(request, id):
    obj = get_object_or_404(aluno, id=id)
    form = AlunoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('listar_alunos')
    return render(request, 'frequencia/form_aluno.html', {'form': form})



def excluir_aluno(request, id):
    obj = get_object_or_404(aluno, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('listar_alunos')
    return render(request, 'frequencia/confirmar_exclusao.html', {'obj': obj})


# ==========================
# CRUD FREQUÊNCIA
# ==========================

def listar_frequencias(request):
    freq = frequencia.objects.all()
    return render(request, 'frequencia/listar_frequencias.html', {'freq': freq})


def adicionar_frequencia(request):
    form = FrequenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_frequencias')
    return render(request, 'frequencia/form_frequencia.html', {'form': form})


def editar_frequencia(request, id):
    obj = get_object_or_404(frequencia, id=id)
    form = FrequenciaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('listar_frequencias')
    return render(request, 'frequencia/form_frequencia.html', {'form': form})


def excluir_frequencia(request, id):
    obj = get_object_or_404(frequencia, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('listar_frequencias')
    return render(request, 'frequencia/confirmar_exclusao.html',  {'obj': obj})
