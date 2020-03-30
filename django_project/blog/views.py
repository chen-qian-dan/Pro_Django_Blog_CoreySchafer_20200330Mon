from django.shortcuts import render

def home(request): # handle the traffic from home page.
    return render(request, 'blog/home.html')


def about(request): # about page
    return render(request, 'blog/about.html')