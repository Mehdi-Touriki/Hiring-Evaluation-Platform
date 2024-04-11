from django.contrib.auth.models import User
from django.db import models


class Recruiter(User):
    nom_entreprise = models.CharField(max_length=100)

    def __str__(self):
        return self.username
