from users.models import User
from django.utils import timezone
from django.db import models
from django.urls import reverse
from datetime import datetime

JOB_CATEGORIES = [
    ('category1', 'Information and Technology'),
    ('category2', 'Finance and Accounting'),
    ('category3', 'Human Resources'),
    ('category4', 'Health and Medical'),
    ('category5', 'Construction and Public Works'),
    ('category6', 'Hospitality and Catering'),
    ('category7', 'Logistics and Transportation'),
    ('category8', 'Media and Communication'),
    ('category9', 'Art and Design'),
    ('category10', 'Costumer Services'),
]

CATEGORY_MAP = {v: k for k, v in JOB_CATEGORIES}


class Post(models.Model):
    job_category = models.CharField(max_length=50, choices=JOB_CATEGORIES)
    job_title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    job_location = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.IntegerField(null=True, blank=True)
    publication_data = models.DateField(default=timezone.now)
    requirements = models.TextField()
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_title

    def get_absolute_url(self):
        return reverse('jobs:job_description', kwargs={'pk': self.pk})


def upload_to(instance, filename):
    now = datetime.now()
    return f"website/cvs/{now.year}/{now.month}/{filename}"


class ApplyJob(models.Model):
    application_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cv = models.FileField(upload_to=upload_to)
    job = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    date = models.DateField(default=timezone.now)
    score_technique = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('jobs:job_apply', kwargs={'pk': self.pk})


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profil'

    def get_absolute_url(self):
        return reverse('jobs:profil')


class SavedPostt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    saved_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'saved_post')
