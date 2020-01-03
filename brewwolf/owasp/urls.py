from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('messageboard', views.Messageboard, name='messageboard'),
    path('vote', views.Vote, name='vote') 
]
