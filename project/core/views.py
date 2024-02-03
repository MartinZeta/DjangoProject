#from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import *

# Create your views here.
def index(request):
    contexto = {}
    return render(request, "core/index.html")

#crear vista de about.html
#def about(request: HttpRequest) -> HttpResponse:
    #return render(request, "core/about.html")
    
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'core/login.html'
    
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "core/index.html")
    else:
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})
    