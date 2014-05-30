from django.shortcuts import render, get_object_or_404, redirect
from .models import Message, UserFollowingRelationship
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm, PostMessageForm
from django.core.exceptions import ObjectDoesNotExist
from django.forms.util import ErrorList
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

def home(request):
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
                pass_error = True
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
                user = authenticate(username=username, password=pass1)
                if user is not None:
                    if user.is_active:
                        auth_login(request, user)
            return redirect('/')

    return render(request, "register.html", locals())

def login(request):
    data = request.POST if request.POST else None
    form = LoginForm(data)
    wrong_user = False
    if request.method == 'POST':
        if form.is_valid():
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    redirect('home')
                redirect('home')
            else:
                wrong_user = True
                return render(request, "login.html", locals())
        return redirect('/')
    return render(request, "login.html", locals())

def logout(request):
    auth_logout(request)
    return redirect('/')

@login_required
def users(request):
    all_users = User.objects.all()
    followed_users = [usr.followed for usr in UserFollowingRelationship.objects.all().filter(follower__username=request.user.username)]
    not_followed_users = []
    for usr in all_users:
        if usr not in followed_users:
            not_followed_users.append(usr)

    return render(request, "users.html", locals())

@login_required
def follow(request, follow_user):
    if not UserFollowingRelationship.objects.filter(follower__username=request.user.username, followed__username=follow_user).exists():
        followed_user = User.objects.all().filter(username=follow_user).first()
        follow_relationship = UserFollowingRelationship(follower=request.user, followed=followed_user)
        follow_relationship.save()
    return redirect('/users')

@login_required
def unfollow(request, unfollow_user):
    try:
        UserFollowingRelationship.objects.filter(follower__username=request.user.username, followed__username=unfollow_user).delete()
    except:
        pass
    return redirect('/users')

@login_required
def messages(request):
    followed_users = [user.followed.username for user in UserFollowingRelationship.objects.filter(follower__username=request.user.username).all()]
    all_messages_from_followed_users = Message.objects.filter(author__username__in=followed_users).order_by('-pub_date')[:10]
    return render(request, "messages.html", locals())

@login_required
def createmessage(request):
    data = request.POST if request.POST else None
    form = PostMessageForm(data)
    if request.method == 'POST':
        if form.is_valid():
            text = form.cleaned_data['text']
            location = form.cleaned_data['location']
            message = Message(author=request.user, text=text, location=location)
            message.save()
        return redirect('/messages/')

    return render(request, "createmessage.html", locals())

def about(request):
    return render(request, "about.html", locals())

def contact(request):
    return render(request, "contact.html", locals())

@login_required
def mymessages(request):
    my_messages = Message.objects.filter(author=request.user).order_by('-pub_date')
    return render(request, "mymessages.html", locals())

@login_required
def delete_message_by_id(request, message_id):
    message_to_delete = Message.objects.get(id=message_id)
    if message_to_delete.author == request.user:
        message_to_delete.delete()
    return redirect('/mymessages')
