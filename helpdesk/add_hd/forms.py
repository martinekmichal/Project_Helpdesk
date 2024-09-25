from django import forms
from .models import Helpdesk



class HelpdeskForm(forms.ModelForm):
    class Meta:
        model = Helpdesk
        fields = ['jmeno', 'telefon']

