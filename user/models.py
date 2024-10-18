from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(default='<EMAIL>')
    name = models.CharField(max_length=100, default='User')
    weight = models.FloatField(default=0, validators=[])
    height = models.FloatField(default=0)
    preferences = models.CharField(max_length=255, default='')
    diseases = models.CharField(max_length=255, default='')
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Change this to a unique name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Change this to a unique name
        blank=True
    )
