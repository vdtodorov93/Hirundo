from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
#from django.db import models

class RegisterForm(ModelForm):

    password = forms.CharField()
    password_check = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']
