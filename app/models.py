from django.db import models
from django.contrib.auth.models import AbstractUser


class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class UserGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UniversityUser(AbstractUser):
    role_type = models.CharField(max_length=40, choices=[
        ('teacher', 'Teacher'),
        ('student', 'Student')
    ])
    subject = models.ForeignKey(Subject, related_name='title', on_delete=models.CASCADE, default=None, null=True, blank=True)
    group = models.ManyToManyField(UserGroup, default=None, blank=True)

    def __str__(self):
        return self.username
