from .form import RegisterUserFormCandidat, RegisterUserFormRecruter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .form import *


def home(request):
    return render(request, "home.html")


# def signuprec(request):
# return render(request, "recruteur/signuprec.html")


# def signupcan(request):
# return render(request, "candidat/signupcan.html")
def home_can(request):
    return render(request, "users/candidat/jobs.html")


def home_rec(request):
    return render(request, "users/recruteur/index.html")


def post_job(request):
    return render(request, "recruteur/formulaire.html")


def login(request):
    # return render(request, "login.html")
    form = UserLoginForm(request.POST or None)

    if request.user.is_authenticated:
        return redirect('/')

    else:
        if request.method == 'POST':
            if form.is_valid():
                auth.login(request, form.get_user())
                return HttpResponseRedirect(get_success_url(request))
    context = {
        'form': form,
    }

    return render(request, 'login.html', context)


# Sign up de candidat:

def register_candidat(request):
    if request.method == "POST":
        print("hello")
        form = RegisterUserFormCandidat(request.POST)
        print(form.is_valid())
        if form.is_valid():
            var = form.save(commit=False)
            var.save()
            firstname = form.cleaned_data.get('prenom')
            lastname = form.cleaned_data.get('nom')
            messages.success(request, f"Account created for {lastname} {firstname}!")
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong when trying to register')
            return redirect('register_candidat')
    else:
        form = RegisterUserFormCandidat()
    return render(request, 'users/candidat/signupcan.html', {'form': form})


def register_recruter(request):
    if request.method == 'POST':
        form = RegisterUserFormRecruter(request.POST)
        if form.is_valid():
            form.save()
            firstname = form.cleaned_data.get('prenom')
            lastname = form.cleaned_data.get('nom')
            messages.success(request, f"Account created for {lastname} {firstname}!")
            redirect('post_job')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('register_recruter')
    else:
        form = RegisterUserFormRecruter()
        return render(request, 'users/recruteur/signuprec.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'You are Successfully logged out')
    return redirect('users:login')
