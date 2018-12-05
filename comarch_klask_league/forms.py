from django import forms
from django.core.exceptions import ValidationError

from .models import Player

class NewPlayerForm(forms.ModelForm):
    first_name = forms.CharField(max_length=64, label="Imię")
    last_name = forms.CharField(max_length=64, label="Nazwisko")
    
    class Meta:
        model = Player
        fields = ['first_name', 'last_name']
        
    def clean_first_name(self):
        return self.data.get('first_name').strip()   
        
    def clean_last_name(self):
        return self.data.get('last_name').strip()
        
    def clean(self):
        fn = self.clean_first_name()
        ln = self.clean_last_name()
        if Player.objects.filter(first_name=fn, last_name=ln).exists():
            raise ValidationError("Zawodnik {0} {1} już istnieje!".format(fn, ln))
        else:
            return self.cleaned_data
        
        
class NewMatchForm(forms.Form):
    winner = forms.ModelChoiceField(queryset=Player.objects.all(), label="Zwycięzca")
    looser = forms.ModelChoiceField(queryset=Player.objects.all(), label="Przegrany")
    
    def clean(self):
        winner = self.data.get('winner')
        looser = self.data.get('looser')
        if winner == looser:
            raise ValidationError("Nie możesz rozegrać meczu z samym sobą!")
        else:
            return self.cleaned_data
