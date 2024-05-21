import os
from django.conf import settings
from django import forms
from django.contrib.auth import get_user_model
from .models import ApplyJob, Post
import json

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
        fields = ['job_category', 'job_title', 'job_type', 'job_location', 'publication_data',
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


class QuizForm(forms.Form):
    question = forms.CharField(label='Question',
                               widget=forms.Textarea(attrs={'readonly': 'readonly',
                                                            'class': 'form-control',
                                                            'cols': 100,
                                                            'rows': 3
                                                            }))
    choices = forms.ChoiceField(widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        question_value = self.initial.get('question', '')
        self.fields['choices'].choices = choices_from_question(question_value)


def choices_from_question(question: str) -> list[tuple[str, str]]:
    file_path = os.path.join(settings.BASE_DIR, 'jobs', 'static', 'json', 'quiz.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            questions = json.load(file)
    except FileNotFoundError:
        raise Exception(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise Exception(f"Error decoding JSON from file: {file_path}")
    for i in range(len(questions)):
        if questions[i]['question'] == question:
            return [(str(j), questions[i]['choices'][j]) for j in range(len(questions[i]['choices']))]
