from django.db import models


class User(models.Model):
    jmeno = models.CharField(max_length=100)
    telefon = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title


class Helpdesk(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
