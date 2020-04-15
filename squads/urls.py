from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:squad_id>', views.detail, name='detail'),
    path('<int:squad_id>/upvote', views.upvote, name='upvote'),
]
