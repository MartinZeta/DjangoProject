#El modulo "views.py" trabaja la logica interna, se vincula views con "models.py" 
# para trabajar con esos modelos. Tambien esta vinculado a "index.html" donde se muestran los templates

from django.shortcuts import render

#Se importa Cliente para usar el modelo
from . import models
#Se importa ClienteForm para usar el modelo forms.py que son los formularios.
from . import forms


# Create your views here.


def index(request):
    return render(request, "cliente/index.html")
                                                 #clientes es la key que usamos para iterar en el "index.html"

def cliente_list(request):
    clientes = models.Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, "cliente/cliente_list.html", context)


def pais_list(request):
    paises = models.Pais.objects.all()
    context = {"paises": paises}
    return render(request, "cliente/pais_list.html", context)

def cliente_create(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:cliente_list")
    else:  # if request.method == "GET":
        form = forms.ClienteForm()
    return render(request, "cliente/cliente_create.html", {"form": form})