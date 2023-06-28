from django import forms
from GameStats.Games.models import Game


class GameForm(forms.ModelForm):
    creator = forms.CharField(disabled=True)

    class Meta:
        model = Game
        fields = '__all__'

