from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from users.models import (Recruiter)


class Post(models.Model):
    job_title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    job_location = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.IntegerField(null=True, blank=True)
    publication_data = models.DateField(default=timezone.now)
    requirements = models.TextField()
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_title


# Create your models here.
class Apply_job(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cv = models.FileField()

    def __str__(self):
        return self.name
