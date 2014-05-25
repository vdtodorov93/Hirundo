from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
#from django.db import models

class RegisterForm(ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    password_check = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
