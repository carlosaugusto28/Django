from django.shortcuts import render, redirect
from .models import Cliente
from .models import Computadore

def home(request):
    Clientes = Cliente.objects.all()
    Computadores = Computadore.objects.all()
    return render(request, "index.html",{"Clientes": Clientes})

def salvar(request):
    vnome = request.POST.get("nome")
    Cliente.objects.create(nome=vnome)
    Clientes = Cliente.objects.all()
    return render(request, "index.html", {"Clientes": Clientes})
    
def editar(request, id):
    Clientes = Cliente.objects.get(id=id)
    return render(request, "update.html", {"Cliente": Clientes})

def update(request, id):
    vnome = request.POST.get("nome")
    Clientes = Cliente.objects.get(id=id)
    Clientes.nome = vnome
    Clientes.save()
    return redirect(home)

def delete(request, id):
    Clientes = Cliente.objects.get(id=id)
    Clientes.delete()
    return redirect(home)