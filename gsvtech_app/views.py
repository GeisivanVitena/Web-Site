from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "gsvtech_app/partial/home.html")


def sobre(request):
    return render(request, "gsvtech_app/partial/sobre.html")

def servicos(request):
    return render(request, "gsvtech_app/partial/servicos.html")

def contato(request):
    return render(request, "gsvtech_app/partial/contato.html")


def welcome(request):
    return render(request, "gsvtech_app/partial/welcome.html")

