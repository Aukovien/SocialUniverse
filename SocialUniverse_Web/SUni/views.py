from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<p>home</p')

def contact(request):
    return HttpResponse('<p>contact</p>')

def about(request):
    return HttpResponse('<p>about</p>')

def login(request):
    return HttpResponse('<p>login</p>')

