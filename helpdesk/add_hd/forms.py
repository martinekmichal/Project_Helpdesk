from django import forms
from .models import Helpdesk


class HelpdeskForm(forms.ModelForm):
    class Meta:
        model = Helpdesk
        fields = [ 'jmeno_zadatele', 'datum_zalozeni', 'termin_splneni', 'popis_problemu', 'resitel', 'vyjadreni', 'zpracovano']
        widgets = {
            'jmeno_zadatele': forms.TextInput(attrs={'class': 'form-control'}),
            'termin_splneni': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'datum_zalozeni': forms.DateInput(attrs={'class': 'form-control', 'type': 'date','readonly': 'readonly'}),
            'popis_problemu': forms.Textarea(attrs={'class': 'form-control', 'rows':10}),
            'resitel': forms.Select(attrs={'class': 'form-control'}),
            'vyjadreni': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'zpracovano': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'jmeno_zadatele': 'Jméno žadatele:',
            'datum_zalozeni': 'Datum založení:',
            'termin_splneni': 'Termín splnění:',
            'popis_problemu': 'Popis problému:',
            'resitel': 'Řešitel:',
            'vyjadreni': 'Vyjádření:',
            'zpracovano': 'Zpracováno:',
        }

