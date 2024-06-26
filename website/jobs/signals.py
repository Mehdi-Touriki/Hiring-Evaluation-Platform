from django.db.models.signals import post_save
from users.models import User
from django.dispatch import receiver
from .models import Profil


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if hasattr(instance, 'Profil'):
        instance.Profil.save()