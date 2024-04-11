from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from .models import User


class RegisterUserFormRecruter(UserCreationForm):
    model = get_user_model()  # recruiter ilyass
    nom = forms.CharField()
    prenom = forms.CharField()
    entreprise = forms.CharField()
    username = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()  # this is the "YourCustomUser" that you imported at the top of the file
        fields = ('username', 'password1', 'password2', 'nom', 'prenom', 'entreprise')


class RegisterUserFormCandidat(UserCreationForm):
    model = get_user_model()
    nom = forms.CharField()
    prenom = forms.CharField()
    username = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()  # this is the "YourCustomUser" that you imported at the top of the file
        fields = ('username', 'password1', 'password2', 'nom', 'prenom')
