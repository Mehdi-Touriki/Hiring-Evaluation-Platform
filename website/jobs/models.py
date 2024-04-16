from users.models import User
from django.utils import timezone
from django.db import models
from django.urls import reverse


class Post(models.Model):
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
    



class ApplyJob(models.Model):
    application_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cv = models.FileField(upload_to='website/cvs')
    job = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('jobs:job_apply', kwargs={'pk': self.pk})