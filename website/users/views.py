from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .form import RegisterUserFormCandidat,RegisterUserFormRecruter
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, "home.html")


#def signuprec(request):
    #return render(request, "recruteur/signuprec.html")


#def signupcan(request):
    #return render(request, "candidat/signupcan.html")
def home_can(request):
    return render(request, "users/candidat/jobs.html")
def home_rec(request):
    return render(request, "users/recruteur/index.html")
def post_job(request):
    return render(request, "recruteur/formulaire.html")
def login(request):
    return render(request, "login.html")
def description(request):
    # todo: fill the context parameter
    return render(request, "candidat/description.html", context={})


#Sign up de candidat:

def register_candidat(request):
    if request.method== "POST":
        form=RegisterUserFormCandidat(request.POST)
        if form.is_valid():
            form.save()
            firstname=form.cleaned_data.get('prenom')
            lastname=form.cleaned_data.get('nom')
            messages.success(request,f"Account created for {lastname} {firstname}!") 
            return  redirect('jobs')
        else:
          messages.warning(request,'Something went wrong')
          return redirect('home') 
    else:
     form=RegisterUserFormCandidat()
    return render(request,'users/candidat/signupcan.html',{'form':form})
    
def register_recruter(request):
    if request.method== 'POST':
        form=RegisterUserFormRecruter(request.POST)
        if form.is_valid():
            form.save()
            firstname=form.cleaned_data.get('prenom')
            lastname=form.cleaned_data.get('nom')
            messages.success(request,f"Account created for {lastname} {firstname}!") 
            redirect('post_job')
        else:
          messages.warning(request,'Something went wrong')
          return redirect('register_recruter')
    else: 
        form=RegisterUserFormRecruter()
        return render(request,'users/recruteur/signuprec.html',{'form':form})