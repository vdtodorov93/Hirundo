from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Message
#from django.db import models

class RegisterForm(ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    password_check = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class PostMessageForm(ModelForm):

    class Meta:
        model = Message
        fields = ['text', 'location']
        widgets = {
            'text': forms.Textarea(attrs={'rows':2, 'cols':40}),
            'location': forms.Textarea(attrs={'rows':1, 'cols':40}),
        }


