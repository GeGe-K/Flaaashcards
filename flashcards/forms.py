from .models import *
from django import forms

class CardForm(forms.ModelForm):
    class Meta:
        model=Flashcard
        exclude=['username']

class PostCard(forms.ModelForm):
    class Meta:
        model=Flashcard
        exclude=['username']