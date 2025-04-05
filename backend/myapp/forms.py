from django import forms
from .models import *

class ULoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class TrainersCreateForm(forms.ModelForm):
    class Meta:
        model = Trainers
        fields = ['trainer_name', 'role','quote', 'photo']
        widgets = {
                #     'category':forms.Select(attrs={'class':'col-md-5'}),
                   'trainer_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'role': forms.TextInput(attrs={'class': 'form-control'}),
                   'quote': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
                   
                   }
