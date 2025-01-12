from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(verbose_name='Username', max_length=50, unique=True)
    first_name = models.CharField(verbose_name='First name', max_length=40)
    last_name = models.CharField(verbose_name='Last name', max_length=40)
    email = models.CharField(verbose_name='Email', max_length=50)
    password = models.CharField(verbose_name='password', max_length=100)
    created = models.DateTimeField(verbose_name='Created data', auto_now_add=True)

    is_staff = models.BooleanField(verbose_name='Is staff', default=False)
    is_active = models.BooleanField(verbose_name='Is active', default=True)
    is_superuser = models.BooleanField(verbose_name='Is superuser', default=False)

    class Meta:
        ordering = ['id', 'username', 'first_name', 'last_name', 'is_active', 'is_staff']


class Book(models.Model):
    title = models.CharField(max_length=150)

    class Meta:
        ordering = ['id', 'title']
