from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = 'home'),
    path("myItems", views.myItems, name = 'myItems'),
    path("aboutMe", views.aboutMe, name = 'aboutMe')
    
]