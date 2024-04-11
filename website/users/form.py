from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class RegisterUserFormRecruter(UserCreationForm):
    # model=get_user_model()
    nom = forms.CharField()
    prenom = forms.CharField()
    entreprise = forms.CharField()
    login = forms.CharField()
    passe = forms.CharField(widget=forms.PasswordInput)
    repass = forms.CharField(widget=forms.PasswordInput)


class RegisterUserFormCandidat(forms.Form):
    model = get_user_model()
    nom = forms.CharField()
    prenom = forms.CharField()
    login = forms.CharField()
    passe = forms.CharField(widget=forms.PasswordInput)
    repass = forms.CharField(widget=forms.PasswordInput)
