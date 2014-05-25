from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Article
        exclude = ['title']
