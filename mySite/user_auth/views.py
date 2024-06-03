from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SignupForm


# VIEWS
# Login view
def user_login(request):
    return render(request, 'login.html')


# Show user details method
def show_user(request):
    print(type(request.user.username))
    return render(request, 'user.html', {
        "username": request.user.username,
        "password": request.user.password})


# Authentication method
def authenticate_user(request):
    '''Login authentication. If user doesn't exist, stay at log in.
       If user exists, show user details view.'''
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )


# User signup/registration method
def user_signup(request):
    '''This view renders the sign up form. If the form is filled correctly,
       details are saved and user is reversed to login. Else, render sign up
       form again.'''
    if request.method == 'GET':
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return HttpResponseRedirect(
                reverse('user_auth:login')
            )
        else:
            return render(request, 'signup.html', {'form': form})
