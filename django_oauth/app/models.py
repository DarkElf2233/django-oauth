from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass


class Book(models.Model):
    title = models.CharField(verbose_name='Название книги', max_length=100)

    class Meta:
        ordering = ['title']
        verbose_name = 'Книга'
        verbose_name_plural = 'Список Книг'
