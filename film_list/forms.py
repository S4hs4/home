from django import forms
from django.forms import ModelForm
from .models import *

class FilmForm(forms.ModelForm):

    class Meta:
        model = Film
        fields = '__all__'
