from django.shortcuts import render, get_object_or_404, redirect
from .models import Message
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.core.exceptions import ObjectDoesNotExist
from django.forms.util import ErrorList

def home(request):
    a = 5
    return render(request, "home.html", locals())

def register(request):
    data = request.POST if request.POST else None
    pass_error = False
    form = RegisterForm(data)

    if request.method == 'POST':
        if form.is_valid():
            pass1 = form.cleaned_data['password']
            pass2 = form.cleaned_data['password_check']
            if pass1 != pass2 or pass1 == None:
                #return redirect('register')
                #form._errors['password'] = ErrorList(u"Password does not match")
                #form.add_error(password, 'Password does not match')
                pass_error = True
                #raise form.ValidationError("The password does not match")
                return render(request, "register.html", locals())

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username, email, pass1)
                user.first_name = first_name
                user.last_name = last_name
                user.save()

            return render(request, "register.html", locals())
        #return redirect('home')

    return render(request, "register.html", locals())



# Create your views here.
