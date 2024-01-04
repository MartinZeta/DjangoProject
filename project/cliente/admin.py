from django.contrib import admin
                          #admin, este modulo es un app que trar django para registrar los modelos

#Importamos los modelos.
from .models import Cliente, Pais

# Register your models here.

#En esta area hay que registrar los modelos creados de la siguiente manera:
admin.site.register(Pais)
admin.site.register(Cliente)
