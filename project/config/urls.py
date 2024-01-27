from django.contrib import admin
from django.urls import include, path
#se importa el modulo saludo para usarlo.


urlpatterns = [
    path("admin/", admin.site.urls),
    #----------------------------------
    #Se crea el path en la url para que envie la info
    #el parametro que toma en comillas es el nombre que tendria la url
    #el 2° parametro que toma es la funcion creada en view que fue importada
    path("", include(("core.urls", "core"))),
                             #cliente es el paquete que incluimos
                                      #urls es el modulo que incluimos
    path("clientes/", include(("cliente.urls", "cliente"))),
    path("productos/", include(("producto.urls", "producto"))),
]

