from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SignupForm


# VIEWS
# Login view
def user_login(request):
    """ Used in urls.py to show login.html upon 'user_auth' url path.
        Handles Http requests & renders login.html in response.
    :param request: HttpRequest
    :type request: Any
    :return: Rendered view of login.html
    :rtype: HttpResponse
    """
    return render(request, 'login.html')


# Show user details method
def show_user(request):
    """ Used in urls.py to show user.html upon 'user.html' url path.
        Handles Http requests & renders user.html in response.
    :param request: HttpRequest
    :type request: Any
    :return: Rendered view of user.html showing user details
    :rtype: HttpResponse
    """
    print(type(request.user.username))
    return render(request, 'user.html', {
        "username": request.user.username,
        "password": request.user.password})


# Authentication method
def authenticate_user(request):
    """ Used in urls.py to authenticate user upon login.
        Handles Http requests & redirects to user.html or back to login.html in response.
        If user doesn't exist, stay at log in.
        If user exists, show user details view.
    :param request: HttpRequest
    :type request: Any
    :return: Redirected to view of user.html or login.html
    :rtype: HttpResponse
    """
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
    """ Used in urls.py to show signup upon 'user_auth/signup.html'
        Handles Http requests & redirects to login.html in response.
        If the form is filled correctly, details are saved and user 
        is reversed to login. Else, render sign up form again.
    :param request: HttpRequest
    :type request: Any
    :return: Redirected to view of login.html or signup.html
    :rtype: HttpResponse
    """
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
