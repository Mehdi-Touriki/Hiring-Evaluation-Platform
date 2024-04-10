from django.db import models

# Create your models here.
class Apply_job(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cv = models.FileField()

    def __str__(self):
        return self.name
