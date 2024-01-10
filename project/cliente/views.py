#El modulo "views.py" trabaja la logica interna, se vincula views con "models.py" 
# para trabajar con esos modelos. Tambien esta vinculado a "index.html" donde se muestran los templates

from django.shortcuts import render

#Se importa Cliente para usar el modelo
from . import models


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

