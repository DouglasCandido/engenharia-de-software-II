from django.shortcuts import render, redirect
from .forms import AlunoForm
from .models import Aluno

# Create your views here.

def aluno_list(request):
    context = {'aluno_list':Aluno.objects.all()}
    return render(request, "aluno/aluno_list.html", context)

def aluno_form(request, id = 0):
    if request.method == "GET":
        if id == 0:  # Se o id passado for 0 (Default), então exibirá um formulário em branco para ser utilizado em uma operação de insert
            form = AlunoForm()
        else: # Se o id passado for diferente de 0, exibirá um formulário preenchido com os dados do Compromisso correspondentes à chave primária referente ao id
            aluno = Aluno.objects.get(pk = id)
            form = AlunoForm(instance = aluno)
        return render(request, "aluno/aluno_form.html", {'form': form})
    else:
        if id == 0: # Operação de inserir um novo Compromisso
            form = AlunoForm(request.POST)
        else: # Operação de atualizar um Compromisso já existente com a chave primária referente ao id com os dados passados pelo formulário na requisição POST
            aluno = Aluno.objects.get(pk = id)
            form = AlunoForm(request.POST, instance = aluno)
        if form.is_valid(): 
            form.save()
        return redirect('/aluno/list')            

def aluno_delete(id):
    aluno = Aluno.objects.get(pk = id)
    aluno.delete()
    return redirect('/aluno/list')


