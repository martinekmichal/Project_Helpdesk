from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta

def get_default_termin_splneni():
    return timezone.now() + timedelta(weeks=1)

class Helpdesk(models.Model):
    datum_zalozeni = models.DateField(default=timezone.now)
    termin_splneni = models.DateField(default=get_default_termin_splneni)
    jmeno_zadatele = models.CharField(max_length=100)
    popis_problemu = models.TextField(default='Není k dispozici')
    resitel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    vyjadreni = models.TextField(blank=True, null=True)
    zpracovano = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.jmeno_zadatele} - {self.datum_zalozeni}"
