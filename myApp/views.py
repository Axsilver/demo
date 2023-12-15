from django.shortcuts import render, HttpResponse
from .models import MyItem

# Create your views here.

def home(request):
    return render(request, "home.html")

def myItems(request):
    items = MyItem.objects.all()
    return render(request, "myitems.html", {"myItems": items})

def aboutMe(request):
    return render(request, "aboutMe.html")

 