# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
   
    return render(request,"index.html")

def background(request):
     return render(request,"blackground.html")

def country(request):
    return HttpResponse("i belongs to india...")

def study(request):
    return HttpResponse("i have don't anything special in computer science.")

def address(request):
    return render(request,"home.html")

def contact(request):
   return render(request, "contact.html")