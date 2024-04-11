from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # email = models.EmailField(unique=False)
    is_recruiter = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)
