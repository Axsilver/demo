from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.home, name = 'home'),
    path("myItems", views.myItems, name = 'myItems'),
    path("aboutMe", views.aboutMe, name = 'aboutMe'),
    path("chat", views.lobby, name="lobby")
    
]