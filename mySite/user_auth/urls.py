from django.urls import path
from . import views

# Setting application name space
app_name = 'user_auth'

# Mapping url path patterns to views
urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user,
        name='authenticate_user'),
    path('user.html', views.show_user, name='show_user'),
    path('signup.html', views.user_signup, name='signup'),
]
