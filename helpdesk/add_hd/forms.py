from django import forms
from django.db import models



class HelpdeskForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['jmeno', 'telefon']

