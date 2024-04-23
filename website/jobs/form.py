from django import forms
from django.contrib.auth import get_user_model
from .models import ApplyJob, Post

User = get_user_model()


class ApplyForm(forms.ModelForm):
    model = get_user_model()  # recruiter ilyass
    cv = forms.FileField()
    name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = ApplyJob
        fields = ['cv', 'name', 'email']


class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['job_title', 'job_type', 'job_location', 'publication_data',
                  'description', 'salary', 'requirements']


class profilupdate(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
