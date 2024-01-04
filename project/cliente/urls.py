from django.urls import path

from .views import index

#app_name es para darle nombre al conjunto de la urls y sepa cual es su direccion para encontrarlo
app_name = "cliente"

urlpatterns = [
                    #name le da el nombre a este path para ubicarlo
    path("", index, name="index"),
]
