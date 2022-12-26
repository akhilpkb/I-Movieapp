from django import forms
from .models import *

class MovieForm(forms.ModelForm):
    class Meta:
        model= Movies
        fields=('name','desc','year','img')
    
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'form-control'})
        }