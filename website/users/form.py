from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', })
    )
    password = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={

        'placeholder': 'Password',
    }))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("User Does Not Exist.")

            if not user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")

            if not user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user


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
