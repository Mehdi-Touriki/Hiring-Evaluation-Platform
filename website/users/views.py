from .models import *
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import *


def home(request):
    return render(request, "home.html")


# def signuprec(request):
# return render(request, "recruteur/signuprec.html")


# def signupcan(request):
# return render(request, "candidat/signupcan.html")
def home_can(request):
    return render(request, "users/candidat/jobs.html")


def post_job(request):
    return render(request, "recruteur/formulaire.html")


def login_user(request):
    print("you are now logging in")
    if request.method == 'POST':

        email = request.POST.get('login')
        password = request.POST.get('pass')
        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            if request.user.is_recruiter:
                return redirect('jobs:post_job')
            elif request.user.is_candidate:
                return redirect('jobs:job_list')
            else:
                return redirect('users:register_candidat')
        else:
            messages.warning(request, 'something went wrong')
            return redirect('users:login')
    return render(request, 'login.html')


# Sign up de candidat:

def register_candidat(request):
    if request.method == "POST":
        print("hello")
        form = RegisterUserFormCandidat(request.POST)
        print(form.is_valid())
        if form.is_valid():
            email = form.cleaned_data.get('username')
            if User.objects.filter(username=email).exists():
                messages.warning(request, 'Email address already exists.')
                return render(request, 'users/candidat/signupcan.html', {'form': form})
            var = form.save(commit=False)
            var.is_candidate = True
            var.first_name = form.cleaned_data.get('prenom')
            var.last_name = form.cleaned_data.get('nom')
            var.email = form.cleaned_data.get('username')
            var.save()
            messages.success(request, f"Account created for {var.last_name} {var.first_name}!")
            print("registration successful")
            return redirect('users:login')
        else:
            print(form.errors)
            messages.warning(request, 'Something went wrong when trying to register')
            return redirect('users:register_candidat')
    else:
        form = RegisterUserFormCandidat()
    return render(request, 'users/candidat/signupcan.html', {'form': form})


def register_recruter(request):
    if request.method == 'POST':
        form = RegisterUserFormRecruter(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.save()
            var.first_name = form.cleaned_data.get('prenom')
            var.last_name = form.cleaned_data.get('nom')
            var.email = form.cleaned_data.get('username')
            var.save()
            messages.success(request, f"Account created for {var.last_name} {var.first_name}!")
            print("registration successful")
            return redirect('users:login')
        else:
            messages.warning(request, 'Something went wrong when trying to register')
            return redirect('users:register_recruter')
    else:
        form = RegisterUserFormRecruter()
    return render(request, 'users/recruteur/signuprec.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'You are Successfully logged out')
    return redirect('users:login')
