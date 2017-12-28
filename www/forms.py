from django import forms
from django.contrib.auth.models import User
from .models import Person, User

# class PersonForm(forms.Form):
    #name = forms.CharField(label='Imię', max_length=100)
    #email = forms.CharField(label='Adres mailowy', max_length=200)
    #title = forms.CharField(label='Stanowisko', max_length=100)
    #image = forms.CharField(label='Image URL', max_length=255)

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email', 'title', 'photo', 'user']

class LoginForm(forms.Form):
    username = forms.CharField(label='Imię', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
