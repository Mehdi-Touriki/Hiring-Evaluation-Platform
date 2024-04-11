from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.models import User


class RegisterUserFormRecruter(UserCreationForm):
    model = User  # recruiter ilyass
    nom = forms.CharField()
    prenom = forms.CharField()
    entreprise = forms.CharField()
    login = forms.CharField()
    passe = forms.CharField(widget=forms.PasswordInput)
    repass = forms.CharField(widget=forms.PasswordInput)


class RegisterUserFormCandidat(UserCreationForm):
    model = User
    nom = forms.CharField()
    prenom = forms.CharField()
    login = forms.CharField()
    passe = forms.CharField(widget=forms.PasswordInput)
    repass = forms.CharField(widget=forms.PasswordInput)
