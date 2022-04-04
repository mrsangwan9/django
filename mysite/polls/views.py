# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def creator(request):
    return HttpResponse("arun sangwan, You're at my place.")


def country(request):
    return HttpResponse("i belongs to india...")

def study(request):
    return HttpResponse("i have don't anything special in computer science.")

def address(request):
    return HttpResponse("that's my address")

def contact(request):
    return HttpResponse("Dev conatct : arunsangwan@gmail.com")