#"Esta carpeta view se crea para crear las funciones o las partes visibles de la pag"

from django.http import HttpResponse
import datetime
import random

def saludo(request):
    return HttpResponse("¡Hola!")


#------------------------------------------------
# Crear una función que solicite mi nombre
# y la muestre en pantalla al ingresar a una url
# diferente a 'saludo'

def saludo2(request):
    nombre = input("Ingresa tu nombre: ")
    return HttpResponse(f"Hola <h1> {nombre} </h1>")


#--------------------------------------------------
#Funcion con parametros pasados desde la URL cuando estamos en el navegador
def nombre(request, nombre, apellido):
    return HttpResponse(f"{apellido.upper()}, {nombre}")


#--------------------------------------------------
#Funcion con parametros pasados directamente de python que se muestran en la vistas

def fecha_hora(request):
    from datetime import datetime
    ahora = datetime.now().strftime(r"%d/%m/%Y %H:%M:%S.%f")
    return HttpResponse(ahora)

#--------------------------------------------------

# Crear una vista que muestre "Has tirado el dado: <numero>"
# Si el número es 6, mostrar una felicitación
# Si no, mostrar que vuelva a intentar
# import random
# randint(1, 6)

def tirar_dado(request):
    import random
    numero_dado = random.randint(1, 6)
    if numero_dado == 6:
        return HttpResponse(f"<h1> Has tirado el dado: 🎲 {numero_dado} ✨ Suerte! </h1>")
    else:
        return HttpResponse(f"<h1> Has tirado el dado: 🎲 {numero_dado} </h1> <br> Sigue intentando")
