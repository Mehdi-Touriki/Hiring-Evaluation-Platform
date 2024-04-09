from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def signuprec(request):
    return render(request, "recruteur/signuprec.html")


def signupcan(request):
    return render(request, "candidat/signupcan.html")
def home_can(request):
    return render(request, "candidat/jobs.html")
def home_rec(request):
    return render(request, "recruteur/index.html")
def post_job(request):
    return render(request, "recruteur/formulaire.html")
def login(request):
    return render(request, "login.html")
def description(request):
    # todo: fill the context parameter
    return render(request, "candidat/description.html", context={})
