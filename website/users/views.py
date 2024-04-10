from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .form import RegisterUserFormCandidat,RegisterUserFormRecruter


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


#Sign up de candidat:

def register_candidat(request):
    if request.methode== 'POST':
        form=RegisterUserFormCandidat(request.POST)
        if form.is_valid():
            form.save()
            firstname=form.cleaned_data.get('prenom')
            lastname=form.cleaned_data.get('nom')
            messages.success(request,f"Account created for {lastname} {firstname}!") 
            redirect('jobs')
        else:
          messages.warning(request,'Something went wrong')
          return redirect('register_candidat')
    else: 
        form=RegisterUserFormCandidat()
        context={'form':form}
        return render(request,'..\templates\candidat\signupcan.html',context)