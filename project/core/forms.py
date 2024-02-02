from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
                #Username y password para el login son obligatorios, se le puede agregar un mail
        fields = ['username', 'password']
        windgets = {                                    #form-control es para darle estilos al input
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        

