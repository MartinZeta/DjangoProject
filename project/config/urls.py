"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
#se importa el modulo saludo para usarlo.
from .views import fecha_hora, nombre, saludo, saludo2, tirar_dado

urlpatterns = [
    path("admin/", admin.site.urls),
    #----------------------------------
    #Se crea el path en la url para que envie la info
    #el parametro que toma en comillas es el nombre que tendria la url
    #el 2° parametro que toma es la funcion creada en view que fue importada
    #----------------------------------
    # path('saludo/', saludo),
    # path('saludo2/', saludo2),
    # path('nombre/<nombre>/<apellido>', nombre),
    # path('fecha_hora/', fecha_hora),
    # path('tirar_dado/', tirar_dado),
    path("", include("core.urls")),
                             #cliente es el paquete que incluimos
                                      #urls es el modulo que incluimos
    path("clientes/", include("cliente.urls")),
]
