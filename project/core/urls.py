#Se copia una parte del codigo de (urls.py) que se encuentra en Proyectodjango para reutilizarla aca.
#Aca estaria guardada la app que creamos, para que sepa que la creamos, hay que ir a settings.py en el proyecto
#y tenemos que colocar el nombre de la app que creamos en insta  INSTALLED_APPS = ['core']
from django.urls import path

from .views import index

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
]
