from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Avoids conflict with default auth.User.groups
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set",  # Avoids conflict with default auth.User.user_permissions
        blank=True,
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
