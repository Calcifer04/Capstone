from django.urls import path
from . import views

# Setting application name space
app_name = 'polls'

# Mapping url path patterns to views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
