from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('choice', views.choice, name='choice'),
    path('characterform', views.characterform, name='characterform'),
    path('adultsignup', views.adultsignup, name='adultsignup'),
    path('studentsignup', views.adultsignup, name='adultsignup'),
]
