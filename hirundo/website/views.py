from django.shortcuts import render, get_object_or_404, redirect
from .models import Message
from django.contrib.auth.models import User
from .forms import RegisterForm

def home(request):
    a = 5
    return render(request, "home.html", locals())

def register(request):
    form = RegisterForm()
    return render(request, 'register.html', locals())



# Create your views here.
