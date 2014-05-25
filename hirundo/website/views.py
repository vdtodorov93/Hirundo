from django.shortcuts import render, get_object_or_404, redirect

def home(request):
    a = 5
    return render(request, "home.html", locals())




# Create your views here.
