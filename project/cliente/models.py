# modulo "models" sirve para manejar o trabajar con la base de datos
from django.db import models
#Models es un modulo que trae varias clases que podemos usar.
#En otras, CharField, DateField, ForeingKey.

# Create your models here.

#la clase "Pais" Hereda la clase "Model", aclaracion, no se 
#puede heredar modulos se heredan clases, pero de la siguiente manera:

class Pais(models.Model):
                   #CharField se utiliza para saber que la variable es de tipo txt.
                            #max_length es un argumento obligatorio
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre

     #permite cambiar en el administrador como se lee la variable.
    class Meta:
        verbose_name = "país"
        verbose_name_plural = "países"


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
                       #DateField se utiliza para saber que la variable es de tipo Numerico.
                                #null=True para que sepa que es opcional.
                                            #blank=True es obligatorio, va en conjunto con null.
    nacimiento = models.DateField(null=True, blank=True)
                           #Foreignkey significa que esta variable hace referencia a otro modelo, osea, pais. 
                                      #Pais es obligatorio como primer argumento
                                                                   #on_delete... se utiliza para que no borre toda la base de datos del cliente si se borra el pais, obligatorio null y blank
                                                                                              #verbose_name permite cambiar en el administrador como se lee la variable.      
    pais_origen_id = models.ForeignKey(Pais, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="país de origen")
                                    
        
    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"
