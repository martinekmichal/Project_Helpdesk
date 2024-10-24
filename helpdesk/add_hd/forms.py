from django import forms
from .models import Helpdesk


class HelpdeskForm(forms.ModelForm):
    class Meta:
        model = Helpdesk
        fields = ['termin_splneni', 'jmeno_zadatele', 'popis_problemu', 'resitel', 'vyjadreni', 'zpracovano']


