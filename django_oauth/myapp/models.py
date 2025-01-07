from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150)

    class Meta:
        ordering = ['id', 'title']
