from django.urls import path
from . import views

# Mapping url path patterns to views
urlpatterns = [
    path('', views.home, name='home'),
    path('cv/', views.my_cv),
    path('contactme/', views.contactme)
]
