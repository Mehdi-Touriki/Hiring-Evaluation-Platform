from django import forms
from django.contrib.auth import get_user_model
from .models import Apply_job

User = get_user_model()


class ApplyForm(forms.ModelForm):
    model = get_user_model()  # recruiter ilyass
    cv = forms.FileField()
    name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = Apply_job
        fields = ['cv', 'name', 'email']
