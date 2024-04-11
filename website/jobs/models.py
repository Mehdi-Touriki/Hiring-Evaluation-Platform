from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
from django.db import models


class Post(models.Model):
    job_title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    job_location = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.IntegerField(null=True, blank=True)
    publication_date = models.DateField(default=timezone.now)
    requirements = models.TextField()
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_title
