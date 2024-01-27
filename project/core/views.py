from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
def index(request):
    contexto = {}
    return render(request, "core/index.html")

#crear vista de about.html
def about(request: HttpRequest) -> HttpResponse:
    return render(request, "core/about.html")