# Generated by Django 5.0.4 on 2024-04-18 15:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Profil',
        ),
    ]
