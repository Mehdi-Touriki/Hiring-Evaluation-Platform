from django.contrib.auth.models import User
from django.db import models


class Recruiter:
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom_entreprise = models.CharField(max_length=100)

    def __str__(self):
        return self.username
