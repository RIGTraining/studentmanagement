from django import forms
from .models import *
from django.contrib.auth.models import User


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

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['course_name', 'duration']
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',  'email','username', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class ClassNameForm(forms.ModelForm):
    class Meta:
        model = ClassName
        fields = ['class_name', 'course',  'trainer','start_date', 'end_date', 'class_status']
        widgets = {
            'class_name': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'trainer': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type':'date', 'class': 'form-control w-50'}),
            'end_date': forms.DateInput(attrs={'type':'date', 'class': 'form-control w-50'}),
            'class_status': forms.Select(attrs={'class': 'form-control'}),
        }        
