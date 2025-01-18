from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.CharField(verbose_name='Email', max_length=50, unique=True)
    password = models.CharField(verbose_name='Password', max_length=100)
    created = models.DateTimeField(verbose_name='Created data', auto_now_add=True)
    username = None

    is_staff = models.BooleanField(verbose_name='Is staff', default=False)
    is_active = models.BooleanField(verbose_name='Is active', default=True)
    is_superuser = models.BooleanField(verbose_name='Is superuser', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ['id', 'email', 'is_active', 'is_staff']


class Book(models.Model):
    title = models.CharField(max_length=150)

    class Meta:
        ordering = ['id', 'title']
