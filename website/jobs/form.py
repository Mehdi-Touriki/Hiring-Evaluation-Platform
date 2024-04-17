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
        fields = ['job_category','job_title', 'job_type', 'job_location', 'publication_data',
                  'description', 'salary', 'requirements']
