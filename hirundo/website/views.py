from django.shortcuts import render, get_object_or_404, redirect
from models import Message
from django.contrib.auth.models import User

def home(request):
    a = 5
    return render(request, "home.html", locals())

def register(request):



# Create your views here.
