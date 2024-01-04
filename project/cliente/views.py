#El modulo "views.py" trabaja la logica interna, se vincula views con "models.py" 
# para trabajar con esos modelos. Tambien esta vinculado a "index.html" donde se muestran los templates

from django.shortcuts import render

#Se importa Cliente para usar el modelo
from .models import Cliente


# Create your views here.


def index(request):
    clientes = Cliente.objects.all()
    return render(request, "cliente/index.html", {"clientes": clientes})
                                                 #clientes es la key que usamos para iterar en el "index.html"
