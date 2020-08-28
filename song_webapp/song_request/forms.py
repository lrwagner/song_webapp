from django import forms

class RehearsalForm(forms.Form):
    song_name = forms.CharField(label='Song', max_length=100)
    