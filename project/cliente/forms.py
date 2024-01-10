#Se importa forms
from django import forms

#Se importa models
from . import models

#De esta manera se crea un formulario con la clase cliente.
class ClienteForm(forms.ModelForm):
    #Subclase meta de ModelForm.
    class Meta:
        #Se pasa el modelo 
        model = models.Cliente
        #Esto quiere decir TODOS LOS CAMPOS de cliente.
        fields = "__all__"