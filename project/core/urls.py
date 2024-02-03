#Se copia una parte del codigo de (urls.py) que se encuentra en Proyectodjango para reutilizarla aca.
#Aca estaria guardada la app que creamos, para que sepa que la creamos, hay que ir a settings.py en el proyecto
#y tenemos que colocar el nombre de la app que creamos en insta  INSTALLED_APPS = ['core']
from django.urls import path
from .views import *
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
                    #name le da el nombre a este path para ubicarlo
    path("", index, name="index"),
                   #TemplateView evita tener que hacer un funcion y redirige directamente al template.
    path("about/", TemplateView.as_view(template_name="core/about.html"), name="about"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="core:index"), name="logout"),
    path("register/", register, name="register"),
]
