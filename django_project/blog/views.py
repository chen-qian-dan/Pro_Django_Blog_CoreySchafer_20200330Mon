from django.shortcuts import render

posts = [
    {
        'author': 'Qian', 
        'title': 'Blog 1: ML',
        'content': 'Machine Learning',
        'date_posted': 'March 31, 2020',
    },
    {
        'author': 'Chen', 
        'title': 'Blog 2: CV',
        'content': 'Computer Vision',
        'date_posted': 'March 31, 2020',
    }
]

def home(request): # handle the traffic from home page.
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context) # then home.html can access posts by the key 'posts'


def about(request): # about page
    return render(request, 'blog/about.html', {'title': 'About'})