from django.shortcuts import render
from django.http import HttpResponse

def home(request): # handle the traffic from home page.
    return render(request, 'blog/home.html')


def about(request): # about page
    return HttpResponse('<h1>Blog About</h1>')